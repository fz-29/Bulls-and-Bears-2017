from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^customerlist/$', customerList, name='customerlist'),
    url(r'^customerdetail/$', customerDetail, name='customerdetail'),
    url(r'^StockHolding/$', stockHolding, name='stockholding'),
    # url(r'^sell/$', sellStocks, name='index'),
    # url(r'^sellinfo/$', sellinfo, name='sellinfo'),
    # url(r'^create/$', createCustomer, name='create'),
]