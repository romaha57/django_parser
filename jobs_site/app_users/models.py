from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    city = models.CharField(max_length=100, verbose_name='город', default='россия')
    language = models.CharField(max_length=100, verbose_name='язык программирования', default='python')

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return f'{self.username} / {self.email}'
