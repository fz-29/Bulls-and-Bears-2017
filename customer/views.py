from django.contrib.auth import login
from allauth.socialaccount.models import SocialAccount
from stockmarket.models import *
from customer.models import *

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.views.decorators.csrf import csrf_exempt

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework.views import APIView

import json

@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes((IsAuthenticated,))
def buyStocks(request, format = None):
	response_data={}
	response_data["message"]="You are logged in."
	return JsonResponse(response_data)

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
		customer.save()
	return render(request, "index.html")

@api_view(["POST"])
def buyinfo(request, format = None):
	#tuples = Company.objects.order_by('name').all()
	#companies_serialized = serializers.serialize('json', tuples)
	#return HttpResponse(companies_serialized, content_type="application/json")
	response_data={}
	try :
		company_id = int(request.POST["id"])
	except Exception as e:
		try:
			company_name = request.POST["name"]
			company_id = Company.objects.get(name=company_name).id;
		except Exception as e:
			response_data["success"]="00"
			return JsonResponse(response_data)
	try:
		tuples = Price.objects.filter( company__id = company_id)
		prices = []
		for tup in tuples:
			p = {}
			p["timestamp"] = tup.timestamp
			p["price"] = tup.stock_price
			prices.append(p)
		response_data["prices"] = prices
	except Exception as e:		
		response_data["success"]="0"
		return JsonResponse(response_data)
	else:
		response_data["success"]="1"
	return JsonResponse(response_data)

@api_view(["POST"])
def sellinfo(request, format = None):
	response_data={}
	return JsonResponse(response_data)

@api_view(["POST"])
def sellStocks(request, format = None):
	response_data={}
	return JsonResponse(response_data)