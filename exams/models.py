from django.db import models
from common.service import BaseAbstractModel
from core.models import Course, Teacher, Subject, StudyGroup, Student
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class SessionModel(BaseAbstractModel):
    """Модель сессии студентов"""

    STATUS_SESSION = (
        ("not_started", "Не началась"),
        ("open", "Открыта"),
        ("close", "Завершена"),
    )

    status = models.CharField(
        max_length=255,
        verbose_name="Статус",
        choices=STATUS_SESSION,
        default="not_started",
    )
    date_start = models.DateField(verbose_name="Начало сессии")
    date_end = models.DateField(verbose_name="Конец сессии")
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="Курс", blank=True, null=True
    )

    def clean_status(self):
        if timezone.now().date() > self.date_end:
            self.status = "close"
        if (
            timezone.now().date() > self.date_start
            and timezone.now().date() < self.date_end
        ):
            self.status = "open"
        else:
            self.status = "not_started"
        return super().clean()

    def clean_date(self):
        if self.date_end <= self.date_start:
            raise ValueError("Дата конца сессии должна быть больше даты начала")
        return super().clean()

    def __str__(self):
        return f"Сессия для группы {self.course} {self.date_start} - {self.date_end}"

    class Meta:
        verbose_name = "Сессия"
        verbose_name_plural = "Сессии"


class Exam(BaseAbstractModel):
    """Модель экзамена"""

    session = models.ForeignKey(
        SessionModel, on_delete=models.CASCADE, verbose_name="Сессия"
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        verbose_name="Предмет",
        related_name="exams",
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        verbose_name="Преподаватель",
        related_name="exams",
    )
    group = models.ForeignKey(
        StudyGroup,
        on_delete=models.CASCADE,
        verbose_name="Учебная группа",
        related_name="exams",
    )
    date = models.DateField(verbose_name="Дата экзамена")

    def __str__(self):
        return f"Экзамен {self.subject} {self.group} {self.date}"

    class Meta:
        verbose_name = "Экзамен"
        verbose_name_plural = "Экзамены"


class MarkExam(BaseAbstractModel):
    """
    Модель оценки экзамена
    """

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        verbose_name="Студент",
        related_name="exam_marks",
    )
    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE,
        verbose_name="Экзамен",
        related_name="marks",
    )
    mark = models.SmallIntegerField(
        "Оценка",
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )

    def __str__(self):
        return f"Оценка {self.mark} {self.student}"

    class Meta:
        verbose_name = "Оценка экзамена"
        verbose_name_plural = "Оценки экзамена"


class RetakeExam(BaseAbstractModel):
    """
    Модель повторной сдачи экзамена
    """

    STATUS_RETAKE_EXAM = (
        ("not_started", "Запланирована"),
        ("open", "Идет сдача"),
        ("close", "Завершена"),
    )

    status = models.CharField(
        max_length=255,
        verbose_name="Статус",
        choices=STATUS_RETAKE_EXAM,
        default="not_started",
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        verbose_name="Студент",
        related_name="retake_exams",
    )
    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE,
        verbose_name="Экзамен",
        related_name="retake_exams",
    )
    mark = models.SmallIntegerField(
        "Оценка",
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )

    date = models.DateTimeField(verbose_name="Дата повторного экзамена")

    def __str__(self):
        return f"Повторная сдача экзамена {self.mark} {self.student}"

    class Meta:
        verbose_name = "Повторная сдача экзамена"
        verbose_name_plural = "Повторные сдачи экзамена"
