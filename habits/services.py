import requests

from config import settings


def send_telegram_message(telegram_id, text):
    """ Отправка сообщения в телеграм """

    URL = 'https://api.telegram.org/bot'
    TOKEN = settings.TELEGRAM_API_TOKEN

    response = requests.post(
        url=f'{URL}{TOKEN}/sendMessage',
        data={
            'chat_id': telegram_id,
            'text': text,
        }
    )


def create_message(habit):
    """ Создание сообщения """

    telegram_id = habit.user.telegram_id
    related_habit = habit.related_habit.get('action')
    reward = habit.reward
    if related_habit:
        text = f'{habit.user.first_name} выполни свою привычку - {habit.action}. После этого выполни приятную привычку {related_habit}'
    elif reward:
        text = f'{habit.user.first_name} выполни свою привычку - {habit.action}. После этого выполни вознаграждение {reward}'
    else:
        text = f'{habit.user.first_name} выполни свою привычку - {habit.action}.'

    return telegram_id, text
