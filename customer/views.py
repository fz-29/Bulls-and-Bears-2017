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
from django.core import serializers

import json

@api_view(["GET"])
def customerList(request, format = None):
	tuples = Customer.objects.all()
	companies_serialized = serializers.serialize('json', tuples)
	return HttpResponse(companies_serialized, content_type="application/json")

@api_view(["GET"])
def customerDetail(request, format = None):
	obj = get_object_or_404(Customer, pk=request.GET.get('id'))
	customer_serialized = serializers.serialize('json', [obj])
	return HttpResponse(customer_serialized[1:-1], content_type="application/json")

@api_view(["GET"])
def stockHolding(request, format = None):
	tuples = StockHolding.objects.filter(customer__pk = request.GET.get('id')).all()
	companies_serialized = serializers.serialize('json', tuples)
	return HttpResponse(companies_serialized, content_type="application/json")
