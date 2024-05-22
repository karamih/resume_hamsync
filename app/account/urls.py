from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterUserView

urlpatterns = [
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register', RegisterUserView.as_view(), name='user-register'),

    path('RefreshToken', TokenRefreshView.as_view(), name='token_refresh')
]
