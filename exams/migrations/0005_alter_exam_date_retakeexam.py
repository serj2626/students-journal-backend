# Generated by Django 5.1 on 2024-11-14 10:09

import django.core.validators
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_alter_course_options"),
        ("exams", "0004_sessionmodel_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exam",
            name="date",
            field=models.DateField(verbose_name="Дата экзамена"),
        ),
        migrations.CreateModel(
            name="RetakeExam",
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
                    models.CharField(
                        choices=[
                            ("not_started", "Запланирована"),
                            ("open", "Идет сдача"),
                            ("close", "Завершена"),
                        ],
                        default="not_started",
                        max_length=255,
                        verbose_name="Статус",
                    ),
                ),
                (
                    "mark",
                    models.SmallIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ],
                        verbose_name="Оценка",
                    ),
                ),
                ("date", models.DateTimeField(verbose_name="Дата повторного экзамена")),
                (
                    "exam",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="retake_exams",
                        to="exams.exam",
                        verbose_name="Экзамен",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="retake_exams",
                        to="core.student",
                        verbose_name="Студент",
                    ),
                ),
            ],
            options={
                "verbose_name": "Повторная сдача экзамена",
                "verbose_name_plural": "Повторные сдачи экзамена",
            },
        ),
    ]
