from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes


def send_confirmation_email(user, frontend_url="http://localhost:3000/confirm_url/"):
    """Send account confirmation email."""
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    confirm_url = f"{frontend_url}{uid}/{token}/"

    send_mail(
        subject="Confirm your email address",
        message=f"Click the link to confirm your email: {confirm_url}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        fail_silently=False,
    )


def send_password_reset_email(user, frontend_url="http://localhost:3000/reset-password/"):
    """Send password reset email."""
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    reset_url = f"{frontend_url}{uid}/{token}/"

    send_mail(
        subject="Password Reset Request",
        message=f"Click the link to reset your password: {reset_url}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        fail_silently=False,
    )
