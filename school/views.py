# Django
from django_filters.rest_framework import DjangoFilterBackend

# Third party
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Local
from .models import Student
from .models import Course
from .models import Registration
from .serializers import StudentSerializer
from .serializers import CourseSerializer
from .serializers import RegistrationSerializerList
from .serializers import RegistrationSerializerCreateAndUpdate
from .serializers import RegistrationsByStudentSerializer
from .serializers import StudentsByCourseSerializer


class StudentsViewset(viewsets.ModelViewSet):
    """Exibindo todos os estudantes"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name', 'cpf']


class CoursesViewset(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name', 'code']
    filterset_fields = ['level']


class RegistrationsViewset(viewsets.ModelViewSet):
    """Exibindo matrículas"""
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializerCreateAndUpdate
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return RegistrationSerializerList
        return super().get_serializer_class()


class RegistrationsByStudent(ListAPIView):
    """Exibindo matrículas de um aluno"""
    serializer_class = RegistrationsByStudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Registration.objects.filter(student=self.kwargs['pk'])
        return queryset


class StudentsByCourse(ListAPIView):
    """Exibindo alunos de um curso"""
    serializer_class = StudentsByCourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Registration.objects.filter(course=self.kwargs['pk'])
        return queryset
