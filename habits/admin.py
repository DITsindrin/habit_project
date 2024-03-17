from django.contrib import admin

from habits.models import Habit


# Register your models here.
@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    fields = (
        'user', 'place', 'time', 'action', 'sign_pleasant_habit', 'related_habit', 'periodicity', 'reward',
        'time_complete', 'sign_publicity',
    )
