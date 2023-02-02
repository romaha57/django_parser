from django.contrib.auth.models import AbstractUser
from django.db import models

from .user_info import LIST_OF_LANGUAGE, LIST_OF_CITIES, DEFAULT_VAlUE_CITY


class User(AbstractUser):
    city = models.CharField(max_length=70, choices=LIST_OF_CITIES, default=DEFAULT_VAlUE_CITY)
    language = models.CharField(max_length=30, choices=LIST_OF_LANGUAGE)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return f'{self.username} / {self.email}'
