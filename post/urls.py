from django.urls import path
from post.views import *

urlpatterns = [
    path('post/', PostList.as_view(), name=PostList.name),
    path('<int:pk>/posts', PostList.as_view(), name=PostList.name),
    path('<int:pk>/posts', PostDetail.as_view(), name=PostDetail.name),
    path('post/add/<int:pk>', PostAdd.as_view(), name=PostAdd.name),
]
