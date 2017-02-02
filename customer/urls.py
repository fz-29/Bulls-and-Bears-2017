from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^buy/$', buyStocks, name='index'),
    url(r'^buyinfo/$', buyinfo, name='buyinfo'),
    url(r'^sell/$', sellStocks, name='index'),
    url(r'^sellinfo/$', sellinfo, name='sellinfo'),
    url(r'^create/$', createCustomer, name='create'),
]