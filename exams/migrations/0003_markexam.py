# Generated by Django 5.1 on 2024-11-13 09:41

import django.core.validators
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_alter_course_options"),
        ("exams", "0002_exam"),
    ]

    operations = [
        migrations.CreateModel(
            name="MarkExam",
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
                    "mark",
                    models.SmallIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ],
                        verbose_name="Оценка",
                    ),
                ),
                (
                    "exam",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="marks",
                        to="exams.exam",
                        verbose_name="Экзамен",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="exam_marks",
                        to="core.student",
                        verbose_name="Студент",
                    ),
                ),
            ],
            options={
                "verbose_name": "Оценка экзамена",
                "verbose_name_plural": "Оценки экзамена",
            },
        ),
    ]
