from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^currentstockprices/$', current_stock_prices, name='index'),
    url(r'^companystockprices/$', company_stock_prices, name='index'),
]