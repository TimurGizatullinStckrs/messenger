from django.db import models


class DateMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время регистрации")
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name="Время последнего изменения профиля")