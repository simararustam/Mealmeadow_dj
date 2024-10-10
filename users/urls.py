from django.urls import path,include
from users.views import (
    RegisterView,
    LoginView,
    test,
    GoogleSignInView,
    RequestPasswordResetView,
    PasswordResetView
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('test/', test, name='test'),
    path("google/",GoogleSignInView.as_view(),name="google"),

    path('password-reset/', RequestPasswordResetView.as_view(), name='password_reset'),
    path('password-reset-confirm/', PasswordResetView.as_view(), name='password_reset_confirm'),

]