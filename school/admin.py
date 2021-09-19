# Django
from django.contrib import admin

# Local
from .models import Student
from .models import Course
from .models import Registration


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rg', 'cpf', 'birth_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 50
    ordering = ('name',)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'level')
    list_display_links = ('id', 'name')
    search_fields = ('code', 'name',)
    list_per_page = 50
    ordering = ('name',)


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'time_course')
    list_display_links = ('id', 'student')
    search_fields = ('student', 'time_course',)
    list_per_page = 50


admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Registration, RegistrationAdmin)
# Register your models here.
