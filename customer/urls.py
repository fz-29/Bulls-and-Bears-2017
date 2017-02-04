from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^customerlist/$', customerList, name='customerlist'),
    url(r'^customerdetail/$', customerDetail, name='customerdetail'),
    # url(r'^customerhistory/$', customerHistory, name='customerhistory'),
    url(r'^stockholding/$', stockHolding, name='stockholding'),
    url(r'^stockshorted/$', stockShorted, name='stockshorted'),
    url(r'^activity/$', customerActivity, name='activity'),
    url(r'^buy/$', buy, name='buy'),
    url(r'^short/$', short, name='short'),
    url(r'^cover/$', cover, name='cover'),
    url(r'^sell/$', sell, name='sell'),
    # url(r'^sell/$', sellStocks, name='index'),
    # url(r'^sellinfo/$', sellinfo, name='sellinfo'),
    url(r'^create/$', createCustomer, name='create'),
]