from django.db import models
from common.service import BaseAbstractModel
from core.models import Student, Teacher

Type_Subject = (
    ("homework", "Домашняя работа проверена"),
    ("suggestion", "Предложение"),
    ("complaint", "Жалоба"),
    ("message", "Новое входящее сообщение"),
    ("session", "Сессия"),
    ("exam", "Экзамен"),
    ("mark", "Оценка"),
    ("feedback", "Ваше обращение принято"),
    ("subscription", "Вы успешно подписались на рассылку"),
    ("other", "Другое"),
)


class NotificationStudent(BaseAbstractModel):
    """
    Модель уведомления студента
    """

    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, verbose_name="Студент"
    )
    subject = models.CharField(
        max_length=20, choices=Type_Subject, verbose_name="Тема", default="other"
    )
    message = models.TextField(verbose_name="Сообщение")

    def __str__(self):
        return f"Уведомление студента {self.student}"

    class Meta:
        verbose_name = "Уведомление студента"
        verbose_name_plural = "Уведомления студента"


class NotificationTeacher(BaseAbstractModel):
    """
    Модель уведомления преподавателя
    """

    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, verbose_name="Сотрудник"
    )
    subject = models.CharField(
        max_length=20, choices=Type_Subject, verbose_name="Тема", default="other"
    )
    message = models.TextField(verbose_name="Сообщение")

    def __str__(self):
        return f"Уведомление сотрудника {self.teacher}"

    class Meta:
        verbose_name = "Уведомление преподавателя"
        verbose_name_plural = "Уведомления преподавателя"
