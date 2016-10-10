import base64
import httplib2

from oauth2client.client import OAuth2WebServerFlow
from django.conf import settings
from googleapiclient import discovery

from .models import Email


flow = OAuth2WebServerFlow(client_id=settings.GOOGLE_OAUTH2_CLIENT_ID,
                           client_secret=settings.GOOGLE_OAUTH2_CLIENT_SECRET,
                           scope=settings.GOOGLE_SCOPE,
                           redirect_uri=settings.GOOGLE_REDIRECT_URI)


class NoTokenException(Exception):
    """
    Raised when no API token provided
    """


class GoogleMailService(object):
    DATE_FORMAT = "%a, %d %b %Y %H:%M:%S"

    def __init__(self, token):
        if not token:
            raise NoTokenException
        self.token = token

    def save_emails(self):
        """
        Requests email from Google API for the token and saves them into database
        """
        self._build_service()
        self._process_emails_and_save()

    def _build_service(self):
        """
        Builds gmail service instance via google api discovery
        """
        self.gmail_service = discovery.build('gmail_service', 'v1', http=self.google_auth(self.token))

    def _process_emails_and_save(self):
        """
        Goes through all the email ID, requests data and saves it
        """
        mail_id_list = self.gmail_service.users().messages().list(userId='me').execute()
        for message in mail_id_list.get('messages', []):
            self._save_email(message['id'])

    def _save_email(self, message_id):
        email_data = self._request_email_data(message_id)
        header_map = self._map_headers(email_data)
        body = base64.b64decode(email_data['payload']['body']['data'])

        Email.objects.get_or_create(
            email_id=message_id,
            defaults=dict(
                from_address=header_map.get('From'),
                to_address=header_map.get('To'),
                body=body,
                timestamp=header_map.get('Date')
            )
        )

    def _request_email_data(self, email_id):
        return self.gmail_service.users().messages().get(userId='me', id=email_id).execute()

    @staticmethod
    def _map_headers(my_email):
        return {header['name']: header['value'] for header in my_email['payload']}

    @staticmethod
    def google_auth(token):
        credentials = flow.step2_exchange(token)
        http_req = httplib2.Http()
        return credentials.authorize(http_req)

    @staticmethod
    def _get_header_value(my_email, field_name):
        for header in my_email['payload']['headers']:
            if header['name'] == field_name:
                return header['value']
