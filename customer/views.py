from django.contrib.auth import login
from allauth.socialaccount.models import SocialAccount
from stockmarket.models import *
from customer.models import *

from django.http import HttpResponse, JsonResponse
from django.shortcuts import *
from django.views.decorators.http import require_POST

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.views.decorators.csrf import csrf_exempt

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework.views import APIView
from django.core import serializers

import json

@api_view(["GET"])
def customerList(request, format = None):
	tuples = Customer.objects.all()
	customer_serialized = serializers.serialize('json', tuples)
	return HttpResponse(customer_serialized, content_type="application/json")

@api_view(["GET"])
def customerDetail(request, format = None):
	obj = get_object_or_404(Customer, pk=request.GET.get('id'))
	customer_serialized = serializers.serialize('json', [obj])
	return HttpResponse(customer_serialized[1:-1], content_type="application/json")

@api_view(["GET"])
def stockHolding(request, format = None):
	tuples = StockHolding.objects.filter(customer__pk = request.GET.get('id')).all()
	serialized = serializers.serialize('json', tuples)
	return HttpResponse(serialized, content_type="application/json")

@api_view(["GET"])
def stockShorted(request, format = None):
	tuples = StockHolding.objects.filter(customer__pk = request.GET.get('id')).all()
	serialized = serializers.serialize('json', tuples)
	return HttpResponse(serialized, content_type="application/json")

@api_view(["GET"])
def customerActivity(request, format=None):
	tuples = StockHolding.objects.filter(customer__pk = request.GET.get('id')).all()
	serialized = serializers.serialize('json', tuples)
	return HttpResponse(serialized, content_type="application/json")

def createCustomer(request, format = None):	
	if not request.user.is_authenticated:	
		user = SocialAccount.objects.get(uid = request.GET.get("fbid")).user
		login(request, user)
	else:
		user = request.user
	try:
		customer = Customer.objects.get(user = user)
	except Customer.DoesNotExist:
		customer = Customer(user = user, account_balance = 25000)
		companies = Company.objects.all()
		customer.save()
		for company in companies:
			sh = StockHolding(company=company, customer=customer, quantity=0)
			ss = StockShorted(company=company, customer=customer, quantity=0)
			sh.save()
			ss.save()
	return HttpResponseRedirect('/')
