from django.urls import path

from users.views import UserRegisterAPIView, UserProfileAPIView, UserDestroyAPIView
from users.apps import UsersConfig

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('create/', UserRegisterAPIView.as_view(), name='user-create'),
    path('update/<int:pk>/', UserProfileAPIView.as_view(), name='user-update'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user-delete'),
]
