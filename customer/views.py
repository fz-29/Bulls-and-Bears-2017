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

@api_view(["GET"])
def companyList(request, format = None):
	tuples = Company.objects.order_by('name').all()
	companies_serialized = serializers.serialize('json', tuples)
	return HttpResponse(companies_serialized, content_type="application/json")

@api_view(["GET"])
def customerDetail(request, format = None):
	obj = get_object_or_404(Company, pk=request.GET.get('id'))
	customer_serialized = serializers.serialize('json', [obj])
	return HttpResponse(customer_serialized[1:-1], content_type="application/json")