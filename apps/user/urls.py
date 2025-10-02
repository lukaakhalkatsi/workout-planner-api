from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    RegisterView,
    LoginView,
    ConfirmEmailAPIView,
    ResendConfirmationEmailAPIView,
    PasswordResetRequestView,
    PasswordResetConfirmView,
)

urlpatterns = [
    # User registration & authentication
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Email confirmation
    path('confirm-email/', ConfirmEmailAPIView.as_view(), name='confirm-email'),
    path('resend-confirm-email/', ResendConfirmationEmailAPIView.as_view(), name='resend-confirm-email'),

    # Password reset
    path('password-reset/', PasswordResetRequestView.as_view(), name='password_reset_request'),
    path('password-reset-confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
