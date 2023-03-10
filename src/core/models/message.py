from django.db import models


class Message(models.Model):
    author = models.ForeignKey('User', on_delete=models.PROTECT, related_name="author", verbose_name="Отправитель")
    chat = models.ForeignKey('Chat', on_delete=models.PROTECT, related_name="chat",
                             verbose_name="Чат, содержащий данное сообщение")
    reply_to = models.ForeignKey('Message', on_delete=models.PROTECT, related_name="replied_to", null=True,
                                 verbose_name="Сообщение на которое ответили")
    forward_by = models.OneToOneField('User', on_delete=models.PROTECT, related_name="forward_by", null=True,
                                      verbose_name="Кем сообщение было переслано")
    text = models.CharField(max_length=255, null=True, verbose_name="Текст сообщения")
    picture = models.ImageField(null=True, verbose_name="Картинка сообщения")
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name="Время отправки сообщения")
