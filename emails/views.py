
from django.http import HttpResponse, HttpResponseForbidden
from django.views.generic import TemplateView
from django.views import View
from django.shortcuts import redirect
from rest_framework import viewsets

from emails import services
from .models import Email
from serializer import EmailSerializer


class HomeView(TemplateView):
    template_name = 'base.html'


class GoogleAuth(View):

    def get(self, *args, **kwargs):
        auth_uri = services.flow.step1_get_authorize_url()
        return redirect(auth_uri)


class GoogleReturnAuth(View):

    def get(self, request, *args, **kwargs):
        request.session['TOKEN'] = request.GET.get('code', '')
        return redirect('home')


class EmailsView(View):

    def get(self, request):
        try:
            email_service = services.GoogleMailService(request.session.get('TOKEN'))
            email_service.save_emails()
        except services.NoTokenException:
            return HttpResponseForbidden()
        return HttpResponse('Emails View')


class EmailViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
