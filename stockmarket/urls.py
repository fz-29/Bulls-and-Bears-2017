from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^companylist/$', companyList, name='companylist'),
    url(r'^companydetail/$', companyDetail, name='companyDetail'),
    url(r'^newslist/$', newsList, name='newsList'),
    url(r'^newsdetail/$', newsList, name='newsList'),
    url(r'^companyhistory/$', companyHistory, name='companyhistory'),
    url(r'^loandetail/$', loanDetail, name='loandetail'),
]