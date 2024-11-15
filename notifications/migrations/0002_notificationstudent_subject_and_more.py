# Generated by Django 5.1 on 2024-11-13 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notifications", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="notificationstudent",
            name="subject",
            field=models.CharField(
                choices=[
                    ("homework", "Домашка проверена"),
                    ("suggestion", "Предложение"),
                    ("complaint", "Жалоба"),
                    ("message", "Сообщение"),
                    ("session", "Сессия"),
                    ("exam", "Экзамен"),
                    ("mark", "Оценка"),
                    ("feedback", "Обратная связь"),
                    ("other", "Другое"),
                ],
                default="other",
                max_length=20,
                verbose_name="Тема",
            ),
        ),
        migrations.AddField(
            model_name="notificationteacher",
            name="subject",
            field=models.CharField(
                choices=[
                    ("homework", "Домашка проверена"),
                    ("suggestion", "Предложение"),
                    ("complaint", "Жалоба"),
                    ("message", "Сообщение"),
                    ("session", "Сессия"),
                    ("exam", "Экзамен"),
                    ("mark", "Оценка"),
                    ("feedback", "Обратная связь"),
                    ("other", "Другое"),
                ],
                default="other",
                max_length=20,
                verbose_name="Тема",
            ),
        ),
    ]
