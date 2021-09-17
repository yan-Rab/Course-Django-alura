# Django
from django.urls import path
from django.urls.conf import include

# Third party
from rest_framework.routers import DefaultRouter

# Local
from .views import StudentsViewset
from .views import CoursesViewset
from .views import RegistrationsViewset
from .views import RegistrationsByStudent
from .views import StudentsByCourse

router = DefaultRouter()

router.register(r'students', StudentsViewset, basename='students')
router.register(r'courses', CoursesViewset, basename='courses')
router.register(r'registrations', RegistrationsViewset, basename='registrations')

urlpatterns = [
    path('api/school/', include([
        *router.urls,
        path('student/<int:pk>/courses', RegistrationsByStudent.as_view(), name='student-registrations'),
        path('course/<int:pk>/students', StudentsByCourse.as_view(), name='course-students')
    ]))
]
