from django.shortcuts import render
from rest_framework import generics

from habits.models import Habit
from habits.serializers import HabitSerializer


# Create your views here.


class HabitListAPIView(generics.ListAPIView):
    """ Вывод списка привычек """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitCreateAPIView(generics.CreateAPIView):
    """ Создание списка привычки """
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """ Просмотр одной привычки """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitUpdateAPIView(generics.UpdateAPIView):
    """ Изменение привычки """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitDestroyAPIView(generics.DestroyAPIView):
    """ Удаление привычки """
    queryset = Habit.objects.all()
