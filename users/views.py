from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import (
    RegisterSerializer, 
    LoginSerializer, 
    GoogleSignInSerializer,
    PasswordResetRequestSerializer,
    PasswordResetSerializer
)
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.generics import GenericAPIView



User = get_user_model()
token_generator = PasswordResetTokenGenerator()


def test(request):
    return render(request, 'test.html')

class RegisterView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=RegisterSerializer,
        responses={
            201: 'User registered successfully', 
            400: 'Bad Request'
        },
    )

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=LoginSerializer,
        responses={200: openapi.Response('JWT Token', schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'refresh': openapi.Schema(type=openapi.TYPE_STRING, description='Refresh Token'),
                'access': openapi.Schema(type=openapi.TYPE_STRING, description='Access Token'),
            },
        )),
        400: 'Invalid credentials'},
    )

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GoogleSignInView(GenericAPIView):
    serializer_class = GoogleSignInSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        print("data",serializer.validated_data)
        data=((serializer.validated_data)['access_token'])
        return Response(data, status=status.HTTP_200_OK)

class RequestPasswordResetView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=PasswordResetRequestSerializer,
        responses={
            200: openapi.Response('Password reset link sent successfully'),
            400: openapi.Response('Invalid email'),
        }
    )

    def post(self, request, *args, **kwargs):
        serializer = PasswordResetRequestSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(email=serializer.validated_data['email'])
            token = token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            # Send email (simplified, adjust this to your needs)
            reset_url = f"http://127.0.0.1:8000/api/reset-password/{uid}/{token}/"
            send_mail(
                'Password Reset Request',
                f'Click the link to reset your password: {reset_url}',
                'from@example.com',
                [user.email],
                fail_silently=False,
            )
            return Response({"message": "Password reset link has been sent to your email."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PasswordResetView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=PasswordResetSerializer,
        responses={
            200: openapi.Response('Password reset successfully'),
            400: openapi.Response('Invalid token or other errors'),
        }
    )

    def post(self, request, *args, **kwargs):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            uidb64 = request.data.get('uid')
            token = request.data.get('token')
            password = serializer.validated_data['password']

            try:
                uid = force_str(urlsafe_base64_decode(uidb64))
                user = User.objects.get(pk=uid)
            except (TypeError, ValueError, OverflowError, User.DoesNotExist):
                return Response({"error": "Invalid link"}, status=status.HTTP_400_BAD_REQUEST)

            if token_generator.check_token(user, token):
                user.set_password(password)
                user.save()
                return Response({"message": "Password reset successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
