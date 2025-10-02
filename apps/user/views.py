from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth.tokens import default_token_generator

from .models import User
from .serializers import (
    RegisterSerializer, LoginSerializer,
    ConfirmEmailSerializer, ResendEmailSerializer,
    PasswordResetEmailSerializer, PasswordResetConfirmSerializer
)
from .utils import send_confirmation_email, send_password_reset_email
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['Authentication'])
class RegisterView(APIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        send_confirmation_email(user)
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)


@extend_schema(tags=['Email Confirmation'])
class ConfirmEmailAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = ConfirmEmailSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        uidb64 = serializer.validated_data['uidb64']
        token = serializer.validated_data['token']

        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response({"error": "Invalid link."}, status=status.HTTP_400_BAD_REQUEST)

        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save(update_fields=["is_active"])
            return Response({"message": "Email confirmed successfully."}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid or expired token."}, status=status.HTTP_400_BAD_REQUEST)



@extend_schema(tags=['Email Confirmation'])
class ResendConfirmationEmailAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = ResendEmailSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "User with this email does not exist."}, status=status.HTTP_400_BAD_REQUEST)

        if user.is_active:
            return Response({"message": "User is already active."}, status=status.HTTP_400_BAD_REQUEST)

        send_confirmation_email(user)
        return Response({"message": "Confirmation email resent."}, status=status.HTTP_200_OK)


@extend_schema(tags=['Authentication'])
class LoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]

        if not user.is_active:
            return Response(
                {"detail": "Email is not verified. Please check your inbox."},
                status=status.HTTP_403_FORBIDDEN
            )

        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }, status=status.HTTP_200_OK)


@extend_schema(tags=['Password Management'])
class PasswordResetRequestView(APIView):
    permission_classes = [AllowAny]
    serializer_class = PasswordResetEmailSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'detail': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        send_password_reset_email(user)
        return Response({'detail': 'Password reset email sent.'}, status=status.HTTP_200_OK)


@extend_schema(tags=['Password Management'])
class PasswordResetConfirmView(APIView):
    permission_classes = [AllowAny]
    serializer_class = PasswordResetConfirmSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        uidb64 = serializer.validated_data['uidb64']
        token = serializer.validated_data['token']
        new_password = serializer.validated_data['new_password']

        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response({'detail': 'Invalid user ID.'}, status=status.HTTP_400_BAD_REQUEST)

        if not default_token_generator.check_token(user, token):
            return Response({'detail': 'Invalid token.'}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save(update_fields=["password"])
        return Response({'detail': 'Password has been reset successfully.'}, status=status.HTTP_200_OK)
