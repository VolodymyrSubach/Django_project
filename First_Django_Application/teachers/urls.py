from django.urls import path

from teachers.views import create_teacher
from teachers.views import delete_teacher
from teachers.views import detail_teacher
from teachers.views import get_teacher
from teachers.views import update_teacher

app_name = 'teacher'

urlpatterns = [
    path('', get_teacher, name='list'),
    path('create/', create_teacher, name='create'),
    path('detail/<int:teacher_id>/', detail_teacher, name='detail'),
    path('update/<int:teacher_id>/', update_teacher, name='update'),
    path('delete/<int:teacher_id>/', delete_teacher, name='delete'),
]
