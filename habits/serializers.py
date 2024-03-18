from rest_framework import serializers

from habits.models import Habit
from habits.validators import RelatedRewardHabitValidator, RelatedPleasantHabitValidator, TimelimitHabitValidator, \
    PleasantHabitValidator, PeriodicityHabitValidator


class HabitSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели привычки """

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            RelatedRewardHabitValidator(),
            RelatedPleasantHabitValidator(),
            TimelimitHabitValidator(),
            PleasantHabitValidator(),
            PeriodicityHabitValidator()
        ]
