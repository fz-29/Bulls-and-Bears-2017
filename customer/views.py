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
	return JsonResponse({"status" : True})