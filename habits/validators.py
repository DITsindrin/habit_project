from datetime import timedelta

from rest_framework.serializers import ValidationError


class RelatedRewardHabitValidator:
    """Исключить одновременный выбор связанной привычки и указания вознаграждения"""

    def __call__(self, value):
        related_habit = value.get('related_habit')
        reward = value.get('reward')

        if related_habit and reward:
            raise ValidationError('Вы должны указать либо связанную привычку, либо признак приятной привычки, '
                                  'или указать принак приятной привычки')


class TimelimitHabitValidator:
    """Время выполнения должно быть не больше 120 секунд."""

    time = timedelta(minutes=2)

    def __call__(self, value):
        time_complete = value.get('time_complete')

        if timedelta(minutes=time_complete.minute) > self.time:
            raise ValidationError('Время на выполнение не более 2х минут')


class RelatedPleasantHabitValidator:
    """В связанные привычки могут попадать только привычки с признаком приятной привычки"""

    def __call__(self, value):
        related_habit = value.get('related_habit')

        if related_habit and not related_habit.sign_pleasant_habit:
            raise ValidationError('В связанные привычки могут попадать только привычки с признаком приятной привычки')


class PleasantHabitValidator:
    """У приятной привычки не может быть вознаграждения или связанной привычки."""

    def __call__(self, attrs):
        sign_pleasant_habit = attrs.get('sign_pleasant_habit')
        related_habit = attrs.get('related_habit')
        reward = attrs.get('reward')
        if sign_pleasant_habit:
            if related_habit or reward:
                raise ValidationError(
                    'У приятной привычки не может быть вознаграждения или связанной привычки.')


class PeriodicityHabitValidator:
    """Нельзя выполнять привычку реже, чем 1 раз в 7 дней"""

    def __call__(self, attrs):
        periodicity = attrs.get('periodicity')
        if periodicity > 7:
            raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')
