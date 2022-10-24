from django.urls import path

from students.views import CreateStudentView, DeleteStudentView, DetailStudentView

from .views import ListStudentView
from .views import UpdateStudentView

app_name = 'students'

urlpatterns = [
    path('', ListStudentView.as_view(), name='list'),
    path('create/', CreateStudentView.as_view(), name='create'),
    path('detail/<int:pk>/', DetailStudentView.as_view(), name='detail'),
    path('update/<int:pk>/', UpdateStudentView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteStudentView.as_view(), name='delete'),
]
