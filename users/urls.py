from django.urls import path

from users.views import UserRegisterAPIView, UserProfileAPIView, UserDestroyAPIView
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('create/', UserRegisterAPIView.as_view(), name='user-create'),
    path('update/<int:pk>/', UserProfileAPIView.as_view(), name='user-update'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user-delete'),
]
