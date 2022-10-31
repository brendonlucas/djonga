from django.contrib.auth.models import User
from rest_framework import serializers, generics, permissions, status
from rest_framework.response import Response

from usuario.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class FuncionarioSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="Funcionario-detail")
    user = UserSerializer()

    class Meta:
        model = Usuario
        fields = ('url', 'pk', 'nome', 'telefone', 'user')


class AddUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Usuario
        fields = ('nome', 'telefone', 'user')
