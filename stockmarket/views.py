from django.shortcuts import *
from .models import *

from django.http import HttpResponse, JsonResponse
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
def companyList(request, format = None):
	# if not request.user.is_authenticated:
	# 	raise Http404
	tuples = Company.objects.order_by('name').all()
	companies_serialized = serializers.serialize('json', tuples)
	return HttpResponse(companies_serialized, content_type="application/json")

# @api_view(["GET"])
def companyDetail(request, format = None):
	if not request.user.is_authenticated:
		raise Http404
	obj = get_object_or_404(Company, pk=request.GET.get('id'))
	company_serialized = serializers.serialize('json', [obj])
	return HttpResponse(company_serialized[1:-1], content_type="application/json")

# @api_view(["GET"])
def companyHistory(request, format = None):
	if not request.user.is_authenticated:
		raise Http404
	tuples = CompanyHistory.objects.filter(company__pk=request.GET.get('id')).order_by('timestamp').all()
	company_history_serialized = serializers.serialize('json', tuples)
	return HttpResponse(company_history_serialized, content_type="application/json")

# @api_view(["GET"])
def loanDetail(request, format = None):
	if not request.user.is_authenticated:
		raise Http404
	obj = get_object_or_404(Loan, customer__pk=request.GET.get('id'))
	loan_serialized = serializers.serialize('json', [obj])
	return HttpResponse(loan_serialized[1:-1], content_type="application/json")

# @api_view(["GET"])
def newsList(request, format = None):
	if not request.user.is_authenticated:
		raise Http404
	tuples = News.objects.filter(is_published=True).order_by('-published_on').all()
	news_serialized = serializers.serialize('json', tuples)
	return HttpResponse(news_serialized, content_type="application/json")

# @api_view(["GET"])
def newsDetail(request, format=None):
	if not request.user.is_authenticated:
		raise Http404
	obj = get_object_or_404(News, pk=request.GET.get('id'))
	news_serialized = serializers.serialize('json', [obj])
	return HttpResponse(news_serialized[1:-1], content_type="application/json")

# @api_view(["GET"])
def newsLatest(request, format=None):
	if not request.user.is_authenticated:
		raise Http404
	obj = News.objects.filter(is_published=True).order_by('-published_on').all().first()
	news_serialized = serializers.serialize('json', [obj])
	return HttpResponse(news_serialized[1:-1], content_type="application/json")

