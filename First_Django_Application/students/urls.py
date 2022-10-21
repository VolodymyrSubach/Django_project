from django.urls import path

from students.views import create_student
from students.views import delete_student
from students.views import detail_student

from .views import ListStudentView
from .views import UpdateStudentView

app_name = 'students'

urlpatterns = [
    path('', ListStudentView.as_view(), name='list'),
    path('create/', create_student, name='create'),
    path('detail/<int:student_id>/', detail_student, name='detail'),
    path('update/<int:pk>/', UpdateStudentView.as_view(), name='update'),
    path('delete/<int:student_id>/', delete_student, name='delete'),
]
