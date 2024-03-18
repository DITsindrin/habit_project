from datetime import datetime

from django.db import models

from users.models import User

# Create your models here.
PERIODICITY_CHOICES = (
    (1, 'раз в день'),
    (2, 'раз в два дня'),
    (3, 'раз в три дня'),
    (4, 'раз в четыре дня'),
    (5, 'раз в пять дней'),
    (6, 'раз в шесть дней'),
    (7, 'раз в семь дней')
)


class Habit(models.Model):
    """ Модель привычки """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель привычки')
    place = models.CharField(max_length=150, verbose_name='Место выполнения привычки')
    time = models.TimeField(verbose_name='Время, когда необходимо выполнять привычку')
    action = models.CharField(max_length=150, verbose_name='Действие')
    sign_pleasant_habit = models.BooleanField(default=False, verbose_name='Признак приятной привычки')
    related_habit = models.ForeignKey('habits.Habit', on_delete=models.SET_NULL, verbose_name='Связанная привычка',
                                      null=True, blank=True)
    periodicity = models.IntegerField(choices=PERIODICITY_CHOICES, verbose_name='Периодичность выполнения привычки')
    reward = models.CharField(max_length=150, verbose_name='Вознаграждение', null=True, blank=True)
    time_complete = models.TimeField(verbose_name='Время на выполнение привычки')
    sign_publicity = models.BooleanField(default=False, verbose_name='Признак публичности')
    action_date = models.DateField(default=datetime.now().date(), verbose_name="Дата действия")

    def __str__(self):
        return f'Я {self.user} буду {self.action} {self.periodicity} в {self.time} - {self.place} - {self.time_complete}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
        ordering = ('id',)
