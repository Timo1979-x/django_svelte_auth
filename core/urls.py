from django.urls import path

from .views import (
    GoogleAuthAPIView,
    LogoutAPIView,
    RefreshAPIView,
    RegisterAPIView,
    LoginAPIView,
    TwoFactorAPIView,
    ForgotAPIView,
    UserAPIView,
    ResetAPIView,
)

urlpatterns = [
    path("register", RegisterAPIView.as_view()),
    path("login", LoginAPIView.as_view()),
    path("two-factor", TwoFactorAPIView.as_view()),
    path("google-auth", GoogleAuthAPIView.as_view()),
    path("user", UserAPIView.as_view()),
    path("refresh", RefreshAPIView.as_view()),
    path("logout", LogoutAPIView.as_view()),
    path("forgot", ForgotAPIView.as_view()),
    path("reset", ResetAPIView.as_view()),
]
