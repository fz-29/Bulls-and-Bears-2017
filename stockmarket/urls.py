from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^companylist/$', companyList, name='companylist'),
    url(r'^allnews/$', all_news, name='allnews'),
    url(r'^companystockprices/$', company_stock_prices, name='index'),
]