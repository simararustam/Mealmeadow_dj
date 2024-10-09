from google.auth.transport import requests
from google.oauth2 import id_token
from users.models import User
from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

class Google():
    @staticmethod
    def validate(access_token):
        try:
            idinfo = id_token.verify_oauth2_token(access_token, requests.Request())
            if "accounts.google.com " in idinfo['iss']:
                return idinfo
        except Exception as e:
            return "Token is invalid or expired"
        
def login_social_user(email,password):
    user = authenticate(email=email, password=password)
    user_tokens = user.tokens()
    return {
        "email": user.email,
        "first_name": user.get_full_name,
        "access": str(user_tokens.get("access_token")),
        "refresh": str(user_tokens.get("refresh_token")),
    }
        
def register_social_user(provider, email, name, last_name):
    user = User.objects.filter(email=email)
    if user.exists():
        if provider == user[0].auth_providers:
            login_social_user(email, settings.SOCIAL_AUTH_PASSWORD)
        else:
            raise AuthenticationFailed(detail="Please continue your login using " + user[0].auth_providers)
    else:
        new_user = {
            "email": email,
            "name": name,
            "last_name": last_name,
            "password": settings.SOCIAL_AUTH_PASSWORD,
        }
        register_user = User.objects.create_user(**new_user)
        register_user.auth_providers = provider
        register_user.save()
        login_social_user(email= register_user.email, password= settings.SOCIAL_AUTH_PASSWORD)