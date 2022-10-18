from django.urls import path

from groups.views import create_group
from groups.views import delete_group
from groups.views import detail_group
# from groups.views import get_group

from .views import ListGroupView
from .views import UpdateGroupView

app_name = 'group'

urlpatterns = [
    path('', ListGroupView.as_view(), name='list'),
    path('create/', create_group, name='create'),
    path('detail/<int:group_id>/', detail_group, name='detail'),
    path('update/<int:pk>/', UpdateGroupView.as_view(), name='update'),
    path('delete/<int:group_id>/', delete_group, name='delete'),
]
