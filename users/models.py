from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')

    telegram_id = models.CharField(max_length=250, verbose_name='Telegram id', null=True, blank=True)
    phone = models.CharField(max_length=35, verbose_name='Telephone number', null=True, blank=True)
    city = models.CharField(max_length=80, verbose_name='City', null=True, blank=True)
    avatar = models.ImageField(upload_to='users/', default='users.png', verbose_name='Avatar')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email} {self.telegram_id}'
