from django.contrib import admin
from .models import Inbox, Message, ImageMessage


@admin.register(Inbox)
class InboxAdmin(admin.ModelAdmin):
    """
    Админ Класс Переписка
    """

    list_display = ("get_first_user", "get_second_user")

    def get_first_user(self, obj):
        return obj.users.first()

    def get_second_user(self, obj):
        return obj.users.last()

    get_first_user.short_description = "Первый пользователь"
    get_second_user.short_description = "Второй пользователь"


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """
    Админ Класс Сообщения
    """

    list_display = (
        "inbox",
        "sender",
        "receiver",
        "text",
        "is_read",
    )


@admin.register(ImageMessage)
class ImageMessageAdmin(admin.ModelAdmin):
    """
    Админ Класс Фото
    """

    list_display = ("image",)
