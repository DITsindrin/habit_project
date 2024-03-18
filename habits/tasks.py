from datetime import datetime, timedelta
from celery import shared_task
from django.utils import timezone

from habits.models import Habit
from habits.services import send_telegram_message, create_message


@shared_task
def send_message_habit_telegram():
    """ Задача для получения привычек, создания сообщения и отправка в телеграм пользователю """
    habits = Habit.objects.all().filter(sign_of_pleasant=False)
    date = datetime.now().date()
    time_up = timezone.now() - timedelta(minutes=5)
    time_after = timezone.now() + timedelta(minutes=5)

    for habit in habits:
        if habit.action_date <= date:
            if time_up <= habit.time <= time_after:
                telegram_id, text = create_message(habit)
                send_telegram_message(telegram_id, text)
                habit.action_date = date + timedelta(days=habit.periodicity)
                habit.save()
