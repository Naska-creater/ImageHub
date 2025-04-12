from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from account.managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255,blank= False, verbose_name='Имя')
    second_name = models.CharField(max_length=255,blank= False, verbose_name='Фамилия')
    nick_name = models.CharField(max_length=255,unique=True)
    email = models.CharField(max_length=255,blank= False, unique=True)
    phone = models.CharField(max_length=255, unique=True, verbose_name='Телефон')
    password = models.CharField(max_length=255, verbose_name='Пароль')
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    def __str__(self):
        return f'Пользователь: {self.nick_name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
