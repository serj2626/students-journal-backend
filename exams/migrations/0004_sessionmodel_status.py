# Generated by Django 5.1 on 2024-11-14 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exams", "0003_markexam"),
    ]

    operations = [
        migrations.AddField(
            model_name="sessionmodel",
            name="status",
            field=models.CharField(
                choices=[
                    ("not_started", "Не началась"),
                    ("open", "Открыта"),
                    ("close", "Завершена"),
                ],
                default="not_started",
                max_length=255,
                verbose_name="Статус",
            ),
        ),
    ]
