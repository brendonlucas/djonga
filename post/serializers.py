from django.contrib.auth.models import User
from rest_framework import serializers, generics, permissions, status
from rest_framework.response import Response

from post.models import Post
from usuario.models import *
from usuario.serializers import FuncionarioSerializer


class PostSerializer(serializers.ModelSerializer):
    dono = FuncionarioSerializer()

    class Meta:
        model = Post
        fields = ('title', 'descricao', 'foto', 'dono')


class AddPostSerializer(serializers.ModelSerializer):


    class Meta:
        model = Post
        fields = ('title', 'descricao', 'foto')
