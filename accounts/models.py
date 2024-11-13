from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    """
    Модель пользователя
    """

    user_type_data = [
        ("admin", "Админ"),
        ("teacher", "Преподаватель"),
        ("student", "Студент"),
    ]
    user_type = models.CharField(
        choices=user_type_data,
        max_length=30,
        default="student",
        verbose_name="Тип пользователя",
    )
    online = models.BooleanField(default=False, verbose_name="онлайн")
