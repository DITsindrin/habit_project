import datetime

import requests
from celery import shared_task
from django.utils import timezone

from config import settings
from habits.models import Habit


@shared_task
def habits_every_day():
    habits = Habit.objects.all().filter(periodicity=1).filter(sign_pleasant_habit=False)

    if habits.exists():
        for habit in habits:
            time_up = timezone.now() - datetime.timedelta(minutes=5)
            time_after = timezone.now() + datetime.timedelta(minutes=5)
            time_begin_habit = habit.time

            if time_up <= time_begin_habit <= time_after:
                telegram_id = habit.user.telegram_id
                related_habit = habit.related_habit.get('action')
                reward = habit.reward
                if related_habit:
                    text = f'{habit.user.first_name} выполни свою привычку - {habit.action}. После этого выполни приятную привычку {related_habit}'
                    send_message_habit_telegram(telegram_id=telegram_id, text=text)
                elif reward:
                    text = f'{habit.user.first_name} выполни свою привычку - {habit.action}. После этого выполни вознаграждение {reward}'
                    send_message_habit_telegram(telegram_id=telegram_id, text=text)
                else:
                    text = f'{habit.user.first_name} выполни свою привычку - {habit.action}.'
                    send_message_habit_telegram(telegram_id=telegram_id, text=text)


@shared_task
def every_two_days():
    habits = Habit.objects.all().filter(periodicity=2).filter(sign_pleasant_habit=False)

    if habits.exists():
        for habit in habits:
            time_up = timezone.now() - datetime.timedelta(minutes=5)
            time_after = timezone.now() + datetime.timedelta(minutes=5)
            time_begin_habit = habit.time

            if time_up <= time_begin_habit <= time_after:
                telegram_id = habit.user.telegram_id
                related_habit = habit.related_habit.get('action')
                reward = habit.reward
                if related_habit:
                    text = f'{habit.user.first_name} выполни свою привычку - {habit.action}. После этого выполни приятную привычку {related_habit}'
                    send_message_habit_telegram(telegram_id=telegram_id, text=text)
                elif reward:
                    text = f'{habit.user.first_name} выполни свою привычку - {habit.action}. После этого выполни вознаграждение {reward}'
                    send_message_habit_telegram(telegram_id=telegram_id, text=text)
                else:
                    text = f'{habit.user.first_name} выполни свою привычку - {habit.action}.'
                    send_message_habit_telegram(telegram_id=telegram_id, text=text)


@shared_task
def every_three_days():
    habits = Habit.objects.all().filter(periodicity=3).filter(sign_pleasant_habit=False)

    if habits.exists():
        for habit in habits:
            time_up = timezone.now() - datetime.timedelta(minutes=5)
            time_after = timezone.now() + datetime.timedelta(minutes=5)
            time_begin_habit = habit.time

            if time_up <= time_begin_habit <= time_after:
                telegram_id = habit.user.telegram_id
                related_habit = habit.related_habit.get('action')
                reward = habit.reward
                if related_habit:
                    text = f'{habit.user.first_name} выполни свою привычку - {habit.action}. После этого выполни приятную привычку {related_habit}'
                    send_message_habit_telegram(telegram_id=telegram_id, text=text)
                elif reward:
                    text = f'{habit.user.first_name} выполни свою привычку - {habit.action}. После этого выполни вознаграждение {reward}'
                    send_message_habit_telegram(telegram_id=telegram_id, text=text)
                else:
                    text = f'{habit.user.first_name} выполни свою привычку - {habit.action}.'
                    send_message_habit_telegram(telegram_id=telegram_id, text=text)


@shared_task
def every_four_days():
    habits = Habit.objects.all().filter(periodicity=4).filter(sign_pleasant_habit=False)

    if habits.exists():
        for habit in habits:
            time_up = timezone.now() - datetime.timedelta(minutes=5)
            time_after = timezone.now() + datetime.timedelta(minutes=5)
            time_begin_habit = habit.time

            if time_up <= time_begin_habit <= time_after:
                telegram_id = habit.user.telegram_id
                related_habit = habit.related_habit.get('action')
                reward = habit.reward
                if related_habit:
                    text = f'{habit.user.first_name} выполни свою привычку - {habit.action}. После этого выполни приятную привычку {related_habit}'
                    send_message_habit_telegram(telegram_id=telegram_id, text=text)
                elif reward:
                    text = f'{habit.user.first_name} выполни свою привычку - {habit.action}. После этого выполни вознаграждение {reward}'
                    send_message_habit_telegram(telegram_id=telegram_id, text=text)
                else:
                    text = f'{habit.user.first_name} выполни свою привычку - {habit.action}.'
                    send_message_habit_telegram(telegram_id=telegram_id, text=text)


@shared_task
def every_five_days():
    habits = Habit.objects.all().filter(periodicity=5).filter(sign_pleasant_habit=False)

    if habits.exists():
        for habit in habits:
            time_up = timezone.now() - datetime.timedelta(minutes=5)
            time_after = timezone.now() + datetime.timedelta(minutes=5)
            time_begin_habit = habit.time

            if time_up <= time_begin_habit <= time_after:
                telegram_id = habit.user.telegram_id
                related_habit = habit.related_habit.get('action')
                reward = habit.reward
                if related_habit:
                    text = f'{habit.user.first_name} выполни свою привычку - {habit.action}. После этого выполни приятную привычку {related_habit}'
                    send_message_habit_telegram(telegram_id=telegram_id, text=text)
                elif reward:
                    text = f'{habit.user.first_name} выполни свою привычку - {habit.action}. После этого выполни вознаграждение {reward}'
                    send_message_habit_telegram(telegram_id=telegram_id, text=text)
                else:
                    text = f'{habit.user.first_name} выполни свою привычку - {habit.action}.'
                    send_message_habit_telegram(telegram_id=telegram_id, text=text)


@shared_task
def every_six_days():
    habits = Habit.objects.all().filter(periodicity=6).filter(sign_pleasant_habit=False)

    if habits.exists():
        for habit in habits:
            time_up = timezone.now() - datetime.timedelta(minutes=5)
            time_after = timezone.now() + datetime.timedelta(minutes=5)
            time_begin_habit = habit.time

            if time_up <= time_begin_habit <= time_after:
                telegram_id = habit.user.telegram_id
                related_habit = habit.related_habit.get('action')
                reward = habit.reward
                if related_habit:
                    text = f'{habit.user.first_name} выполни свою привычку - {habit.action}. После этого выполни приятную привычку {related_habit}'
                    send_message_habit_telegram(telegram_id=telegram_id, text=text)
                elif reward:
                    text = f'{habit.user.first_name} выполни свою привычку - {habit.action}. После этого выполни вознаграждение {reward}'
                    send_message_habit_telegram(telegram_id=telegram_id, text=text)
                else:
                    text = f'{habit.user.first_name} выполни свою привычку - {habit.action}.'
                    send_message_habit_telegram(telegram_id=telegram_id, text=text)


@shared_task
def every_seven_days():
    habits = Habit.objects.all().filter(periodicity=7).filter(sign_pleasant_habit=False)

    if habits.exists():
        for habit in habits:
            time_up = timezone.now() - datetime.timedelta(minutes=5)
            time_after = timezone.now() + datetime.timedelta(minutes=5)
            time_begin_habit = habit.time

            if time_up <= time_begin_habit <= time_after:
                telegram_id = habit.user.telegram_id
                related_habit = habit.related_habit.get('action')
                reward = habit.reward
                if related_habit:
                    text = f'{habit.user.first_name} выполни свою привычку - {habit.action}. После этого выполни приятную привычку {related_habit}'
                    send_message_habit_telegram(telegram_id=telegram_id, text=text)
                elif reward:
                    text = f'{habit.user.first_name} выполни свою привычку - {habit.action}. После этого выполни вознаграждение {reward}'
                    send_message_habit_telegram(telegram_id=telegram_id, text=text)
                else:
                    text = f'{habit.user.first_name} выполни свою привычку - {habit.action}.'
                    send_message_habit_telegram(telegram_id=telegram_id, text=text)


@shared_task
def send_message_habit_telegram(telegram_id, text):
    URL = 'https://api.telegram.org/bot'
    TOKEN = settings.TELEGRAM_API_TOKEN

    response = requests.post(
        url=f'{URL}{TOKEN}/sendMessage',
        data={
            'chat_id': telegram_id,
            'text': text,
        }
    )
