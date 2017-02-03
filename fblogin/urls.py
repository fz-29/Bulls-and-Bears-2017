from django.conf.urls import url,include
from django.contrib import admin

from fblogin.views import * 

urlpatterns = [
    url(r'^.*/$', home, name='home'),
]
