# Third party
from rest_framework import serializers

# Local
from .models import Student
from .models import Course
from .models import Registration


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'rg', 'cpf', 'birth_date']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'code', 'name', 'description', 'level']


class RegistrationSerializerList(serializers.ModelSerializer):
    student = StudentSerializer()
    course = CourseSerializer()

    class Meta:
        model = Registration
        fields = ['id', 'student', 'course', 'time_course']


class RegistrationSerializerCreateAndUpdate(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['id', 'student', 'course', 'time_course']


class RegistrationsByStudentSerializer(serializers.ModelSerializer):
    course = serializers.CharField(source='course.name')
    time_course = serializers.SerializerMethodField()

    class Meta:
        model = Registration
        fields = ['course', 'time_course']


    def get_time_course(self, obj):
        return obj.get_time_course_display()


class StudentsByCourseSerializer(serializers.ModelSerializer):
    student = serializers.CharField(source='student.name')

    class Meta:
        model = Registration
        fields = ['student']
