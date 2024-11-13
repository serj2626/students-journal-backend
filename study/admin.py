from django.contrib import admin
from .models import Lesson, MarkLesson, Attendance


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    """
    Админ Класс Посещаемость
    """

    list_display = (
        "lesson",
        "student",
        "status",
    )


@admin.register(MarkLesson)
class MarkAdmin(admin.ModelAdmin):
    """
    Админ Класс Оценки Урока
    """

    list_display = (
        "lesson",
        "student",
        "teacher",
        "value",
    )


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """
    Админ Класс Урок
    """

    list_display = (
        "status",
        "teacher",
        "subject",
        "group",
        "date",
        "created_at",
        "updated_at",
    )
