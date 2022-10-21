from django.urls import path

from groups.views import CreateGroupView
from groups.views import delete_group
from groups.views import detail_group

from .views import ListGroupView
from .views import UpdateGroupView

app_name = 'group'

urlpatterns = [
    path('', ListGroupView.as_view(), name='list'),
    path('create/', CreateGroupView.as_view(), name='create'),
    path('detail/<int:group_id>/', detail_group, name='detail'),
    path('update/<int:pk>/', UpdateGroupView.as_view(), name='update'),
    path('delete/<int:group_id>/', delete_group, name='delete'),
]
