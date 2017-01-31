from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from django.shortcuts import *

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

def home(request, format = None):
    return render(request,"index.html")

