from django.shortcuts import *
from .models import *
from customer.models import *

from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.views.decorators.csrf import csrf_exempt

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework.views import APIView
from django.core import serializers
from ratelimit.decorators import ratelimit

from django.views.decorators.cache import cache_page

import json

@ratelimit(key='ip', rate = '10/m')
@api_view(["GET"])
def companyList(request, format = None):
	tuples = Company.objects.all()
	response_data = {}
	response_data['account_balance'] = "NaN"
	response_data['companies'] = []
	for company in tuples:
		history = CompanyHistory.objects.filter(company=company)
		l = len(history)
		try:
			trend = round((history[l-1].price - history[l-2].price) / company.stock_price * 100, 2) if l > 1 else 0
		except:
			trend = 0
		response_data['companies'].append({
			'id': company.id,
			'symbol': company.symbol,
			'name': company.name,
			'stock_price': company.stock_price,
			'change': history[l-1].price - history[l-2].price if l > 1 else 0,
			'trend': trend,
			'available_quantity': company.available_quantity
		})
	return JsonResponse(response_data)

@ratelimit(key='ip', rate = '10/m')
@api_view(["GET"])
def companyDetail(request, format = None):
	company = get_object_or_404(Company, pk=request.GET.get('id'))
	customer = get_object_or_404(Customer, user=request.user)
	response_data = {}
	response_data['symbol'] = company.symbol
	response_data['name'] = company.name
	response_data['description'] = company.description
	response_data['stock_price'] = company.stock_price
	response_data['available_quantity'] = company.available_quantity
	response_data['annual_growth_rate'] = company.annual_growth_rate
	response_data['market_cap'] = company.market_cap
	response_data['buy_max'] = min(customer.account_balance//company.stock_price, company.available_quantity)
	response_data['sell_max'] = StockHolding.objects.get(customer=customer, company=company).quantity
	response_data['short_max'] = 100
	response_data['cover_max'] = min(StockShorted.objects.get(customer=customer, company=company).quantity, customer.account_balance//company.stock_price)
	response_data['account_balance'] = customer.account_balance
	response_data['price_history'] = []
	response_data['stock_history'] = []
	companyhistory = []
	tuples = CompanyHistory.objects.filter(company__pk=request.GET.get('id')).all()
	tuples = tuples[:60:3] if len(tuples) >= 20 else tuples
	for history in tuples:
		response_data['price_history'].append(history.price)
		response_data['stock_history'].append(history.stocks_available)
	return JsonResponse(response_data)

@cache_page(60)
@ratelimit(key='ip', rate = '10/m')
@api_view(["GET"])
def newsList(request, format = None):
	tuples = News.objects.filter(is_published=True).order_by('-published_on').all()
	news_serialized = serializers.serialize('json', tuples)
	return HttpResponse(news_serialized, content_type="application/json")