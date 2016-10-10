# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from rest_framework import routers
from emails import views

router = routers.DefaultRouter()
router.register(r'emails-data', views.EmailViewSet)


urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^google-auth/$', views.GoogleAuth.as_view(), name='google-auth'),
    url(r'^auth_return/$', views.GoogleReturnAuth.as_view(), name='auth-return'),
    url(r'^emails/$', views.EmailsView.as_view(), name='emails'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),

]
