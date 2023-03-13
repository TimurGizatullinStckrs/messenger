from django.db import models

from core.models import CreatedAtUpdatedAtMixin


class Chat(models.Model, CreatedAtUpdatedAtMixin):
    users = models.ManyToManyField('User', related_name="chats", verbose_name="Участники чата")
    is_dialog = models.BooleanField(default=True, verbose_name="Флаг, является ли чат диалогом")
