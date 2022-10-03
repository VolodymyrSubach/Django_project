from django.urls import path

from students.views import create_student
from students.views import delete_student
from students.views import detail_student
from students.views import get_students
from students.views import update_student

app_name = 'student'

urlpatterns = [
    path('', get_students, name='list'),
    path('create/', create_student, name='create'),
    path('detail/<int:student_id>/', detail_student, name='detail'),
    path('update/<int:student_id>/', update_student, name='update'),
    path('delete/<int:student_id>/', delete_student, name='delete'),
]
