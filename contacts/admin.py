from django.contrib import admin
from .models import Feedback, Subscription


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """Админ Класс Обратная связь"""

    list_display = (
        "user",
        "subject",
        "text",
        "photo",
        "created_at",
    )


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    """Админ Класс Подписка"""

    list_display = (
        "email",
        "created_at",
    )
