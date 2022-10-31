from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from usuario.views import CustomAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuario.urls')),
    # path('api-token-auth/', CustomAuthToken.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('api-token-auth2/', CustomAuthToken.as_view()),

]
