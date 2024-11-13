from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Админ Класс Пользователь"""

    list_display = (
        "email",
        "user_type",
        "username",
        "online",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "is_superuser",
    )
