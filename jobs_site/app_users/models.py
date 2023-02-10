from django.contrib.auth.models import AbstractUser
from django.db import models

from .data_for_create_user import list_languages, list_cities


class User(AbstractUser):
    city = models.CharField(max_length=100, verbose_name='город', choices=list_cities, null=True)
    language = models.CharField(max_length=100, verbose_name='язык программирования', choices=list_languages, null=True)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return f'{self.username} / {self.email}'
