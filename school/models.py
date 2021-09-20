# Django
from django.db import models

# Local
from .constants import LEVELS_VALUES
from .constants import TIME_COURSE_VALUES


class Student(models.Model):
    name = models.TextField(max_length=255)
    rg = models.CharField(max_length=9, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    birth_date = models.DateField()
    cellphone = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.name


class Course(models.Model):
    name = models.TextField(max_length=255)
    code = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    level = models.IntegerField(choices=LEVELS_VALUES)

    def __str__(self):
        return self.name


class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    time_course = models.IntegerField(choices=TIME_COURSE_VALUES)

    def __str__(self) -> str:
        return self.student.name
