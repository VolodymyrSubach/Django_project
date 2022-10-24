from django.urls import path

from groups.views import CreateGroupView, DeleteGroupView, DetailGroupView

from .views import ListGroupView
from .views import UpdateGroupView

app_name = 'group'

urlpatterns = [
    path('', ListGroupView.as_view(), name='list'),
    path('create/', CreateGroupView.as_view(), name='create'),
    path('detail/<int:pk>/', DetailGroupView.as_view(), name='detail'),
    path('update/<int:pk>/', UpdateGroupView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteGroupView.as_view(), name='delete'),
]
