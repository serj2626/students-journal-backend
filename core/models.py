from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save

from common.service import BaseAbstractModel
from .service import get_path_for_avatar
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()


class Course(BaseAbstractModel):
    """
    Модель Курса
    """

    number = models.SmallIntegerField(
        unique=True,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Номер курса",
    )

    def __str__(self):
        return f"Курс {self.number}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ["number"]


class StudyGroup(BaseAbstractModel):
    """
    Модель Учебной Группы
    """

    number = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(4)],
        verbose_name="Номер  учебной группы",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Курс",
        related_name="study_groups",
    )
    slug = models.SlugField(unique=True, verbose_name="Слаг", blank=True, null=True)

    def clean(self):
        if not self.slug:
            self.slug = f"{self.course.number}0{self.number}"
        return super().clean()

    def __str__(self):
        return f"Учебная группа {self.course.number}0{self.number}"

    class Meta:
        verbose_name = "Учебная группа"
        verbose_name_plural = "Учебные группы"
        ordering = ["slug"]
        


class Subject(BaseAbstractModel):
    """
    Модель Предмета
    """

    name = models.CharField(max_length=255, verbose_name="Название предмета")
    slug = models.SlugField(unique=True, verbose_name="Слаг", blank=True, null=True)

    def clean(self):
        if not self.slug:
            self.slug = str(self.name).lower().replace(" ", "-")
        return super().clean()

    def __str__(self):
        return f"Предмет {self.name}"

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"


class Student(BaseAbstractModel):
    """
    Модель студента
    """

    GENDER = (("1", "Мужчина"), ("2", "Женщина"), ("3", "Не указано"))

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    date_of_birth = models.DateField(
        verbose_name="Дата рождения", blank=True, null=True
    )
    gender = models.CharField(
        max_length=255, verbose_name="Пол", choices=GENDER, default=3
    )
    avatar = models.ImageField(
        verbose_name="Аватар",
        upload_to=get_path_for_avatar,
        blank=True,
        null=True,
    )
    address = models.TextField(verbose_name="Адрес", blank=True, null=True)
    phone = models.CharField(
        max_length=255, verbose_name="Телефон", blank=True, null=True
    )
    group = models.ForeignKey(
        StudyGroup,
        on_delete=models.SET_NULL,
        verbose_name="Учебная группа",
        related_name="students",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    def __str__(self):
        return f"Студент {self.user.username}"


class AdminHOD(BaseAbstractModel):
    """
    Модель администратора
    """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    phone = models.CharField(
        max_length=255, verbose_name="Телефон", blank=True, null=True
    )
    avatar = models.ImageField(
        verbose_name="Аватар",
        upload_to=get_path_for_avatar,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"Администратор {self.user.username}"

    class Meta:
        verbose_name = "Админ"
        verbose_name_plural = "Админы"


class Teacher(BaseAbstractModel):
    """
    Модель учителя
    """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    phone = models.CharField(
        max_length=255, verbose_name="Телефон", blank=True, null=True
    )
    Subject = models.ForeignKey(
        Subject,
        on_delete=models.SET_NULL,
        verbose_name="Предмет",
        related_name="teachers",
        blank=True,
        null=True,
    )
    avatar = models.ImageField(
        verbose_name="Аватар",
        upload_to=get_path_for_avatar,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"Персонал {self.user.username}"

    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"


class RaitingTeacher(BaseAbstractModel):
    """Модель рейтинга преподавателя"""

    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        verbose_name="Преподаватель",
        related_name="teacher",
    )
    raiting = models.SmallIntegerField(
        "Оценка",
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )

    def __str__(self):
        return f"{self.teacher.user.username} - {self.raiting}"

    class Meta:
        verbose_name = "Рейтинг преподавателя"
        verbose_name_plural = "Рейтинги преподавателя"
