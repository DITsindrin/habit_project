from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny

from habits.models import Habit
from habits.paginators import HabitPagination
from habits.permissions import IsOwner, IsStaff
from habits.serializers import HabitSerializer


# Create your views here.


class HabitListAPIView(generics.ListAPIView):
    """ Вывод списка привычек """
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    permission_classes = [AllowAny,]

    def get_queryset(self):
        if IsStaff:
            queryset = Habit.objects.all()
            return queryset
        elif IsOwner:
            queryset = Habit.objects.all().filter(user=self.request.user)
            return queryset
        else:
            queryset = Habit.objects.all().filter(sign_publicity=True)
            return queryset


class HabitCreateAPIView(generics.CreateAPIView):
    """ Создание привычки """
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """ Просмотр одной привычки """
    serializer_class = HabitSerializer

    def get_queryset(self):
        if IsStaff:
            queryset = Habit.objects.all()
            return queryset
        elif IsOwner:
            queryset = Habit.objects.all().filter(user=self.request.user)
            return queryset
        else:
            queryset = Habit.objects.all().filter(sign_publicity=True)
            return queryset


class HabitUpdateAPIView(generics.UpdateAPIView):
    """ Изменение привычки """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class HabitDestroyAPIView(generics.DestroyAPIView):
    """ Удаление привычки """
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]
