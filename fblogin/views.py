from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from django.shortcuts import *
from django.contrib.auth.decorators import login_required

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

def login(request, format = None):
    return render(request,"login.html")

@login_required
def home(request):
    return render(request, "index.html")

