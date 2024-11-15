# Generated by Django 5.1 on 2024-11-12 21:07

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_alter_studygroup_options_alter_adminhod_created_at_and_more"),
        ("study", "0002_alter_lesson_created_at_alter_lesson_updated_at_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Attendance",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Создан"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Обновлен"),
                ),
                (
                    "status",
                    models.BooleanField(default=False, verbose_name="Посещаемость"),
                ),
                (
                    "lesson",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attendance",
                        to="study.lesson",
                        verbose_name="Урок",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attendance",
                        to="core.student",
                        verbose_name="Студент",
                    ),
                ),
            ],
            options={
                "verbose_name": "Посещаемость",
                "verbose_name_plural": "Посещаемость",
            },
        ),
    ]
