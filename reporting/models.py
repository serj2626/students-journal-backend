from django.db import models


# class AttendanceReport(models.Model):
#     """
#     Модель отчета посещаемости
#     """

#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     student = models.ForeignKey(
#         Student, on_delete=models.DO_NOTHING, verbose_name="Студент"
#     )
#     attendance = models.ForeignKey(
#         Attendance, on_delete=models.CASCADE, verbose_name="Посещаемость"
#     )
#     status = models.BooleanField(default=False, verbose_name="Статус")
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
#     updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

#     def __str__(self):
#         return f"Отчет посещаемости {self.attendance.attendance_date}"

#     class Meta:
#         verbose_name = "Отчет посещаемости"
#         verbose_name_plural = "Отчеты посещаемости"


# class LeaveReportStudent(models.Model):
#     """
#     Модель отчета о выходе студента
#     """

#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     student = models.ForeignKey(
#         Student, on_delete=models.CASCADE, verbose_name="Студент"
#     )
#     leave_date = models.CharField(max_length=255, verbose_name="Дата выхода")
#     leave_message = models.TextField(verbose_name="Сообщение")
#     leave_status = models.BooleanField(default=False, verbose_name="Статус")
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
#     updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

#     def __str__(self):
#         return f"Отчет о выходе {self.student.user.username}"

#     class Meta:
#         verbose_name = "Отчет о выходе"
#         verbose_name_plural = "Отчеты о выходе"


# class LeaveReportTeacher(models.Model):
#     """
#     Модель отчета о выходе преподавателя
#     """

#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     teacher = models.ForeignKey(
#         Teacher, on_delete=models.CASCADE, verbose_name="Преподаватель"
#     )
#     leave_date = models.CharField(max_length=255, verbose_name="Дата выхода")
#     leave_message = models.TextField(verbose_name="Сообщение")
#     leave_status = models.BooleanField(default=False, verbose_name="Статус")
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
#     updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

#     def __str__(self):
#         return f"Отчет о выходе {self.teacher.user.username}"

#     class Meta:
#         verbose_name = "Отчет о выходе преподавателя"
#         verbose_name_plural = "Отчеты о выходе преподавателя"
