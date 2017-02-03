from django.conf.urls import url,include
from django.contrib import admin

from fblogin.views import * 

urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^$', home, name='home'),
]
