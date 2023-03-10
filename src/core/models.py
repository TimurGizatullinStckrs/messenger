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


class Chat(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания чата")
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name="Время последнего изменения чата")
    users = models.ManyToManyField(User, related_name="users", verbose_name="Участники чата")
    last_message = models.ForeignKey('Message', related_name="last_message", on_delete=models.PROTECT, verbose_name="Последнее сообщение чата")  # on_delete=models.SET(get_last_msg())??
    is_dialog = models.BooleanField(default=True, verbose_name="Флаг, является ли чат диалогом")


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name="author", verbose_name="Отправитель")
    chat = models.ForeignKey(Chat, on_delete=models.PROTECT, related_name="chat", verbose_name="Чат, содержащий данное сообщение")
    reply_to = models.ForeignKey('Message', on_delete=models.PROTECT, related_name="replied_to", null=True, verbose_name="Сообщение на которое ответили")
    forward_by = models.OneToOneField(User, on_delete=models.PROTECT, related_name="forward_by", null=True, verbose_name="Кем сообщение было переслано")
    text = models.CharField(max_length=255, null=True, verbose_name="Текст сообщения")
    picture = models.ImageField(null=True, verbose_name="Картинка сообщения")
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name="Время отправки сообщения")
