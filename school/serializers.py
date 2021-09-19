# Third party
from rest_framework import serializers

# Local
from .models import Student
from .models import Course
from .models import Registration
from .validators import cpf_isvalid
from .validators import name_isvalid
from .validators import rg_isvalid
from .validators import birth_date_isvalid
from .validators import cellphone_isvalid


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'rg', 'cpf', 'birth_date', 'cellphone']

    def validate(self, data):
        if not cpf_isvalid(data['cpf']):
            raise serializers.ValidationError({'cpf': 'O CPF não é válido'})

        if not name_isvalid(data['name']):
            raise serializers.ValidationError({'name': 'Não inclua números neste campo'})

        if not rg_isvalid(data['rg']):
            raise serializers.ValidationError({'rg': 'RG inválido'})

        if not birth_date_isvalid(data['birth_date']):
            raise serializers.ValidationError({'birth_date': 'Data de nascimento inválida'})

        if not cellphone_isvalid(data['cellphone']):
            raise serializers.ValidationError({'cellphone': 'Número inválido'})

        return data

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
