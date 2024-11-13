from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from core.models import Student, Teacher, Subject, StudyGroup
from common.service import BaseAbstractModel


class Lesson(BaseAbstractModel):
    """
    Модель Урока
    """

    LESSON_STATUS = (
        ("1", "Запланирован"),
        ("2", "Проведен"),
        ("3", "Отменен"),
    )

    status = models.CharField(
        max_length=1,
        choices=LESSON_STATUS,
        verbose_name="Статус урока",
        default="1",
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Преподаватель",
        related_name="lessons",
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Предмет",
        related_name="lessons",
    )
    group = models.ForeignKey(
        StudyGroup,
        on_delete=models.CASCADE,
        verbose_name="Учебная группа",
        related_name="lessons",
    )
    date = models.DateTimeField(verbose_name="Дата урока")

    def __str__(self):
        return f"Урок {self.subject.name} {self.study_group}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class MarkLesson(BaseAbstractModel):
    """
    Модель Оценки Урока 
    """

    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name="Урок",
        related_name="marks",
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        verbose_name="Студент",
        related_name="lesson_marks",
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Преподаватель",
        related_name="lesson_marks",
    )
    value = models.SmallIntegerField(
        "Оценка",
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )

    def __str__(self):
        return f"Оценка {self.value} {self.student}"

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"


class Attendance(BaseAbstractModel):
    """
    Модель посещаемости
    """

    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name="Урок",
        related_name="attendance",
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        verbose_name="Студент",
        related_name="attendance",
    )
    status = models.BooleanField(default=False, verbose_name="Посещаемость")

    def __str__(self):
        return f"Посещаемость {self.student}"

    class Meta:
        verbose_name = "Посещаемость"
        verbose_name_plural = "Посещаемость"
