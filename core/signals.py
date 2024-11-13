from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from .models import AdminHOD, Teacher, Student

User = get_user_model()


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     if instance.user_type == "admin":
#         AdminHOD.objects.create(user=instance)
#     elif instance.user_type == "teacher":
#         Teacher.objects.create(user=instance)
#     else:
#         student = Student(user=instance)
#         student.save()
