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