from django.urls import path

from habits.views import HabitListAPIView, HabitCreateAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView
from habits.apps import HabitsConfig

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = HabitsConfig.name

urlpatterns = [
    path('', HabitListAPIView.as_view(), name='habits'),
    path('create/', HabitCreateAPIView.as_view(), name='habit-create'),
    path('retrieve/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit-retrieve'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit-update'),
    path('delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit-delete'),
]
