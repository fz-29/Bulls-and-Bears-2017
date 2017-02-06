from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^companylist/$', companyList, name='companylist'),
    url(r'^companydetail/$', companyDetail, name='companydetail'),
    url(r'^newslist/$', newsList, name='newslist'),
]