from django.test import TestCase
from services import NoTokenException, GoogleMailService


class GoogleServiceTest(TestCase):

    def test_raise_exeption_no_token(self):
        with self.assertRaises(excClass=NoTokenException):
            GoogleMailService(None)
        with self.assertRaises(excClass=NoTokenException):
            GoogleMailService('')
