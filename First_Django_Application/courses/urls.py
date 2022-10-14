from courses.views import create_course
from courses.views import delete_course
from courses.views import detail_course
from courses.views import get_course
from courses.views import update_course

from django.urls import path


app_name = 'course'

urlpatterns = [
    path('', get_course, name='list'),
    path('create/', create_course, name='create'),
    path('detail/<int:course_id>/', detail_course, name='detail'),
    path('update/<int:course_id>/', update_course, name='update'),
    path('delete/<int:course_id>/', delete_course, name='delete'),
]
