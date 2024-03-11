from django.shortcuts import render
from rest_framework import generics
from users.models import User
from users.serializers import UserRegisterSerializer, UserSerializer
from rest_framework.permissions import AllowAny


# Create your views here.
class UserRegisterAPIView(generics.CreateAPIView):
    """ Регистрация пользователя """
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()


class UserProfileAPIView(generics.UpdateAPIView):
    """ Изменение профиля пользователя """
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_update(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()


class UserDestroyAPIView(generics.DestroyAPIView):
    """ Удаление пользователя """
    queryset = User.objects.all()
