from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Админ Класс Пользователь"""

    list_display = (
        "user_type",
        "username",
        "email",
        "first_name",
        "last_name",
        "middle_name",
        "online",
        "is_active",
        "is_staff",
        "is_superuser",
    )

    list_filter = (
        "user_type",
        "is_active",
        "is_staff",
        "is_superuser",
    )

    list_editable = (
        "middle_name",
        "first_name",
        "last_name",
    )



