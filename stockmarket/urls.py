from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^companylist/$', companyList, name='companylist'),
    url(r'^companydetail/$', companyDetail, name='companydetail'),
    url(r'^newslist/$', newsList, name='newslist'),
    url(r'^newsdetail/$', newsList, name='newsdetail'),
    url(r'^latestnews/$', newsLatest, name='newslatest'),
    url(r'^companyhistory/$', companyHistory, name='companyhistory'),
    url(r'^loandetail/$', loanDetail, name='loandetail'),
]