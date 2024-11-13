from django.contrib import admin
from .models import NotificationStudent, NotificationTeacher


@admin.register(NotificationStudent)
class NotificationStudentAdmin(admin.ModelAdmin):
    """
    Админ Класс Уведомление студента
    """

    list_display = ("student", "message", "subject")


@admin.register(NotificationTeacher)
class NotificationTeacherAdmin(admin.ModelAdmin):
    """
    Админ Класс Уведомление преподавателя
    """

    list_display = ("teacher", "message", "subject")
