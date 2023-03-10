from django.db import models


class User(models.Model):
    email = models.CharField(max_length=255, unique=True, verbose_name="Почта пользователя")
    password = models.CharField(max_length=255, verbose_name="Пароль пользователя")
    registered_at = models.DateTimeField(auto_now_add=True, verbose_name="Время регистрации")
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name="Время последнего изменения профиля")
    name = models.CharField(max_length=255, null=True, verbose_name="Имя пользователя")
    surname = models.CharField(max_length=255, null=True, verbose_name="Фамилия пользователя")
    profile_picture = models.ImageField(verbose_name="Фотография профиля")

    def __str__(self):
        return self.email
