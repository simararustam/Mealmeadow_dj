from django.urls import path,include
from users.views import RegisterView, LoginView,test,GoogleSignInView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('test/', test, name='test'),
    path("google/",GoogleSignInView.as_view(),name="google")

]
