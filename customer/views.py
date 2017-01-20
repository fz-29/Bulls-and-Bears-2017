from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.views.decorators.csrf import csrf_exempt

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework.views import APIView

import json

from customer.models import *
from stockmarket.models import *

@api_view(["POST"])
# @authentication_classes([TokenAuthentication])
# @permission_classes((IsAuthenticated,))
def buyStocks(request, format = None):
	customer = get_object_or_404(Customer, user=request.user)
	company = get_object_or_404(Company, pk=request.POST.get('company_id'))
	quantity = int(request.POST.get('quantity'))
	if customer.account_balance <= (company.stock_price * quantity) and 0 < quantity <= company.available_quantity:
		stockHolding = StockHolding.objects.get(customer=customer, company=company)
		stockHolding.quantity += quantity
		customer.account_balance -= company.stock_price * quantity
		company.available_quantity -= quantity
		return JsonResponse({'success':True})
	else:
		return JsonResponse({'success':False})


	