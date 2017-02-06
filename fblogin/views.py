from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from django.shortcuts import *
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.models import SocialAccount
from ratelimit.decorators import ratelimit


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

@ratelimit(key='ip', rate = '10/m')
def login(request, format = None):
    return render(request,"login.html")

@ratelimit(key='ip', rate = '10/m')
@login_required
def home(request):
    context = {
        'fbid': SocialAccount.objects.get(user=request.user).uid,
        'name': request.user.first_name + ' ' + request.user.last_name
    }
    return render(request, "index.html", context)

