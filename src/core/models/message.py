from django.db import models

from core.models import CreatedAtUpdatedAtMixin


class Message(models.Model, CreatedAtUpdatedAtMixin):
    author = models.ForeignKey('User', on_delete=models.SET_NULL, related_name="messages", verbose_name="Отправитель")
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE, related_name="messages",
                             verbose_name="Чат, содержащий данное сообщение")
    replied_to = models.ForeignKey('Message', on_delete=models.SET_NULL, related_name="replied_messages", null=True,
                                   blank=True, verbose_name="Сообщение на которое ответили")
    forwarded_by = models.ForeignKey('User', on_delete=models.SET("DELETED"), related_name="forwarded_messages",
                                     null=True, blank=True, verbose_name="Кем сообщение было переслано") #SET(ENUM.DELETED)???
    text = models.CharField(max_length=255, null=True, blank=True, verbose_name="Текст сообщения")
    picture = models.ImageField(null=True, blank=True, verbose_name="Картинка сообщения", upload_to='chat_pictures')
