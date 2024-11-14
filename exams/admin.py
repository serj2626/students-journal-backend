from django.contrib import admin
from .models import SessionModel, Exam, MarkExam


@admin.register(MarkExam)
class MarkExamAdmin(admin.ModelAdmin):
    """Admin View for MarkExam)"""

    list_display = (
        "student",
        "exam",
        "mark",
    )


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    """
    Админ Класс Экзамен
    """

    list_display = (
        "session",
        "subject",
        "teacher",
        "group",
        "date",
    )


@admin.register(SessionModel)
class SessionModelAdmin(admin.ModelAdmin):
    """
    Админ Класс Сессия
    """

    list_display = (
        "status",
        "date_start",
        "date_end",
        "course",
    )
