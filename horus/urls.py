from django.contrib import admin
from django.urls import path
from horus.views import getData, getEmail, generateLink, Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('horus/<id>/', getData.as_view(), name='horus'),
    path('get/', getEmail.as_view(), name='get'),
    path('link/<id>/', generateLink.as_view(), name='link')
]
