from django.db import models


class Chat(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания чата")
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name="Время последнего изменения чата")
    users = models.ManyToManyField('User', related_name="chats", verbose_name="Участники чата")
    last_message = models.ForeignKey('Message', related_name="last",
                                     on_delete=models.PROTECT, verbose_name="Последнее сообщение чата")
    is_dialog = models.BooleanField(default=True, verbose_name="Флаг, является ли чат диалогом")
