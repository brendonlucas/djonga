from django.urls import path
from usuario.views import *

urlpatterns = [
    path('users/', UserList.as_view(), name=UserList.name),
    path('users/<int:pk>/', UserDetail.as_view(), name=UserDetail.name),
    path('user/add/', UserAdd.as_view(), name=UserAdd.name),
]
