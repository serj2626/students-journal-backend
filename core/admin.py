from django.contrib import admin
from .models import (
    AdminHOD,
    Teacher,
    Student,
    RaitingTeacher,
    StudyGroup,
    Course,
    Subject,
)


@admin.register(StudyGroup)
class StudyGroupAdmin(admin.ModelAdmin):
    """
    Админ Класс Учебная группа
    """

    list_display = (
        "get_full_name",
        "number",
        "course",
        "slug",
        "created_at",
        "updated_at",
    )

    def get_full_name(self, obj):
        return f"Группа {obj.course.number}0{obj.number}"

    get_full_name.short_description = "Название учебной группы"


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """
    Админ Класс Курс
    """

    list_display = (
        "number",
        "created_at",
        "updated_at",
    )


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    """
    Админ Класс Предмет
    """

    list_display = (
        "name",
        "slug",
        "created_at",
        "updated_at",
    )


@admin.register(RaitingTeacher)
class RaitingTeacherAdmin(admin.ModelAdmin):
    """
    Админ Класс Рейтинг преподавателя
    """

    list_display = (
        "teacher",
        "raiting",
        "user",
        "created_at",
        "updated_at",
    )


@admin.register(AdminHOD)
class AdminHODAdmin(admin.ModelAdmin):
    """
    Админ Класс Администратор
    """

    list_display = (
        "user",
        "phone",
        "created_at",
        "updated_at",
    )


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    """
    Админ Класс Преподаватель
    """

    list_display = (
        "user",
        "phone",
        "Subject",
        "created_at",
        "updated_at",
    )


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """
    Админ Класс Студент
    """

    list_display = (
        "user",
        "date_of_birth",
        "gender",
        "phone",
        "group",
        "created_at",
        "updated_at",
    )
