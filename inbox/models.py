from django.db import models
from accounts.models import User
from .service import get_path_for_image_message
from common.service import BaseAbstractModel


class Inbox(BaseAbstractModel):
    """
    Модель Переписки
    """

    users = models.ManyToManyField(
        User, verbose_name="Пользователи"
    )

    class Meta:
        verbose_name = "Переписка"
        verbose_name_plural = "Переписки"

    def __str__(self):
        return f"Переписка {self.sender} - {self.receiver}"


class ImageMessage(BaseAbstractModel):
    """
    Модель Фото
    """

    image = models.ImageField(
        "Фото", upload_to=get_path_for_image_message, blank=True, null=True
    )

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"


class Message(BaseAbstractModel):
    """
    Модель Сообщения
    """

    inbox = models.ForeignKey(
        Inbox,
        on_delete=models.CASCADE,
        related_name="messages",
        verbose_name="Переписка",
    )
    sender = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="sent_messages",
        verbose_name="Отправитель",
        blank=True,
        null=True,
    )
    receiver = models.ForeignKey(
        User,
        related_name="received_messages",
        on_delete=models.SET_NULL,
        verbose_name="Получатель",
        blank=True,
        null=True,
    )
    text = models.TextField("Сообщение", max_length=3000)
    images = models.ManyToManyField(ImageMessage, verbose_name="Фото", blank=True)
    is_read = models.BooleanField("Прочитано", default=False)

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return f"Сообщение {self.sender} - {self.receiver}"
