from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.utils.dateparse import parse_time

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self) -> None:
        # создаем тестового пользователя

        self.user = User.objects.create(email='DITsindrin@mail.ru')
        self.user.set_password('123456')
        self.user.save()

        # аутентифицируем пользователя
        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        """ тестирование создания привычки """

        # отправляем запрос на аутентификацию пользователя
        response = self.client.post('/users/token/', {"email": "DITsindrin@mail.ru", "password": "123456"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        # задаем данные для создания привычки
        data_habit = {
            'user': self.user.pk,
            'place': 'Test',
            'time': parse_time('08:00:00'),
            'action': 'Test',
            'periodicity': 1,
            'time_complete': parse_time('00:02:00'),
        }

        # создаем привычку
        response = self.client.post(
            '/habits/create/',
            data=data_habit
        )

        # print(response.json())

        # проверяем ответ на создание привычки
        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_list_habit(self):
        """ тестирование списка привычек """

        self.maxDiff = None

        # отправляем запрос на аутентификацию пользователя
        response = self.client.post('/users/token/', {"email": "DITsindrin@mail.ru", "password": "123456"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        # создаем тестовую привычку
        Habit.objects.create(
            user=self.user,
            place='Test',
            time=parse_time('08:00:00'),
            action='Test',
            periodicity=1,
            time_complete=parse_time('00:02:00'),
        )

        # получаем список привычек
        response = self.client.get(
            '/habits/'
        )

        # print(response.json())

        # проверяем ответ на получение списка привычек
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_detail_habit(self):
        """ тестирование информации о привычке """

        # отправляем запрос на аутентификацию пользователя
        response = self.client.post('/users/token/', {"email": "DITsindrin@mail.ru", "password": "123456"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        # создаем тестовую привычку
        habit = Habit.objects.create(
            user=self.user,
            place='Test',
            time=parse_time('08:00:00'),
            action='Test',
            periodicity=1,
            time_complete=parse_time('00:02:00'),
        )

        # получаем детали привычки
        response = self.client.get(
            reverse('habits:habit-retrieve', kwargs={'pk': habit.pk})
        )

        # print(response.json())

        # проверяем ответ на получение привычки
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_change_habit(self):
        """ тестирование изменения привычки """

        # отправляем запрос на аутентификацию пользователя
        response = self.client.post('/users/token/', {"email": "DITsindrin@mail.ru", "password": "123456"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        # создаем тестовую привычку
        habit = Habit.objects.create(
            user=self.user,
            place='Test',
            time=parse_time('08:00:00'),
            action='Test',
            periodicity=1,
            time_complete=parse_time('00:02:00'),
        )

        # данные для изменения привычки
        data_habit_change = {
            'user': self.user.pk,
            'place': 'Test_1',
            'time': parse_time('08:00:00'),
            'action': 'Test_1',
            'periodicity': 1,
            'time_complete': parse_time('00:02:00'),
        }

        # получаем детали привычки
        response = self.client.put(
            reverse('habits:habit-update', kwargs={'pk': habit.pk}),
            data=data_habit_change
        )

        # print(response.json())

        # проверяем ответ на получение привычки
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_habit(self):
        """ тестирование удаления привычки """

        # отправляем запрос на аутентификацию пользователя
        response = self.client.post('/users/token/', {"email": "DITsindrin@mail.ru", "password": "123456"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        # создаем тестовую привычку
        habit = Habit.objects.create(
            user=self.user,
            place='Test',
            time=parse_time('08:00:00'),
            action='Test',
            periodicity=1,
            time_complete=parse_time('00:02:00'),
        )

        # получаем детали привычки
        response = self.client.delete(
            reverse('habits:habit-delete', kwargs={'pk': habit.pk})
        )

        # проверяем ответ на получение привычки
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
