# Generated by Django 5.1 on 2024-11-13 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_alter_studygroup_options_alter_adminhod_created_at_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="course",
            options={
                "ordering": ["number"],
                "verbose_name": "Курс",
                "verbose_name_plural": "Курсы",
            },
        ),
    ]
