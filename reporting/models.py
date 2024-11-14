from django.db import models
from study.models import Attendance
from core.models import Student, Teacher
from common.service import BaseAbstractModel


# class LeaveReportStudent(BaseAbstractModel):
#     """
#     Модель отчета о выходе студента
#     """

#     student = models.ForeignKey(
#         Student, on_delete=models.CASCADE, verbose_name="Студент"
#     )
#     leave_date = models.CharField(max_length=255, verbose_name="Дата выхода")
#     leave_message = models.TextField(verbose_name="Сообщение")
#     leave_status = models.BooleanField(default=False, verbose_name="Статус")

#     def __str__(self):
#         return f"Отчет о выходе {self.student.user.username}"

#     class Meta:
#         verbose_name = "Отчет о выходе"
#         verbose_name_plural = "Отчеты о выходе"


# class LeaveReportTeacher(BaseAbstractModel):
#     """
#     Модель отчета о выходе преподавателя
#     """

#     teacher = models.ForeignKey(
#         Teacher, on_delete=models.CASCADE, verbose_name="Преподаватель"
#     )
#     leave_date = models.CharField(max_length=255, verbose_name="Дата выхода")
#     leave_message = models.TextField(verbose_name="Сообщение")
#     leave_status = models.BooleanField(default=False, verbose_name="Статус")

#     def __str__(self):
#         return f"Отчет о выходе {self.teacher.user.username}"

#     class Meta:
#         verbose_name = "Отчет о выходе преподавателя"
#         verbose_name_plural = "Отчеты о выходе преподавателя"
