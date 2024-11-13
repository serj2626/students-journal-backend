from django.db import models
from django.contrib.auth import get_user_model
from common.service import BaseAbstractModel

User = get_user_model()


def get_path_for_photo_feedback(instance, filename) -> str:
    return f"feedback/{instance.user.email}/{instance.id}/{filename}"


class Subscription(BaseAbstractModel):
    """Модель подписки."""

    email = models.EmailField("Почта", max_length=254, unique=True)

    def __str__(self):
        return f"Подписка на новости  от {self.email}"

    class Meta:

        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"


class Feedback(BaseAbstractModel):
    """Модель обратной связи."""

    Type_Subject = (
        ("question", "Вопрос"),
        ("suggestion", "Предложение"),
        ("complaint", "Жалоба"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        blank=True,
        null=True,
    )
    subject = models.CharField(
        "Тема", max_length=200, choices=Type_Subject, default="question"
    )
    text = models.TextField("Сообщение", max_length=1000)
    photo = models.ImageField(
        "Фото", upload_to=get_path_for_photo_feedback, blank=True, null=True
    )

    def __str__(self):
        return f"Обратная связь от {self.user.name}"

    class Meta:

        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"
