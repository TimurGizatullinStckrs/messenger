from django.db import models

from api.serializers import ChatSerializer
from core.models.mixins import DateMixin


class Message(models.Model, DateMixin):
    author = models.ForeignKey('User', on_delete=models.SET_NULL, related_name="messages", verbose_name="Отправитель")
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE, related_name="history",
                             verbose_name="Чат, содержащий данное сообщение")
    replied_to = models.ForeignKey('Message', on_delete=models.SET_NULL, related_name="replied_messages", null=True,
                                   verbose_name="Сообщение на которое ответили")
    forwarded_by = models.ForeignKey('User', on_delete=models.DO_NOTHING, related_name="forwarded_messages", null=True,
                                     verbose_name="Кем сообщение было переслано")
    text = models.CharField(max_length=255, null=True, verbose_name="Текст сообщения")
    picture = models.ImageField(null=True, verbose_name="Картинка сообщения")
