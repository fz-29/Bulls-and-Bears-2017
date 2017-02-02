from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^buy/$', buyStocks, name='index'),
    url(r'^create/$', createCustomer, name='create'),
]