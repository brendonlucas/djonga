from rest_framework.authtoken.models import Token

from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import FileUploadParser
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from post.models import Post
from usuario.models import *
from usuario.serializers import *
from post.serializers import *


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'Post-list'
    # permission_classes = (permissions.IsAuthenticated,)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'Post-detail'
    # permission_classes = (permissions.IsAuthenticated,)


class PostAdd(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = AddPostSerializer
    parser_class = (FileUploadParser, MultiPartParser, FormParser)
    name = 'Add-Post'

    # permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, pk, *args, **kwargs):
        print("akjhsdkjahkjshdkah  askj kas kjdasdhas", pk)
        file_serializer = AddPostSerializer(data=request.data)

        if file_serializer.is_valid():
            print(request.data)
            print(file_serializer.validated_data['foto'])
            usuario = Usuario.objects.get(id=pk)  ################# colocar o token depois
            post = Post(title=file_serializer.data['title'], descricao=file_serializer.data['descricao'],
                        foto=file_serializer.validated_data['foto'], dono=usuario)
            post.save()

            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def post(self, request, *args, **kwargs):
    #     data = AddUserSerializer(data=request.data)
    #     if data.is_valid():
    #         print(data['user']['username'].value)
    #         print(data['user']['password'].value)
    #         print(data['user']['email'].value)
    #         print()
    #         print()
    #         user = User.objects.create_user(username=data['user']['username'].value,
    #                                         password=data['user']['password'].value,
    #                                         email=data['user']['email'].value)
    #         funcionario = Usuario(nome=data['nome'].value, telefone=data['telefone'].value, user=user)
    #         funcionario.save()
    #         return Response(data.data, status=status.HTTP_201_CREATED)
    #     else:
    #         try:
    #             user = User.objects.get(username=data['user']['username'].value)
    #             if user:
    #                 return Response({'error': 'usuario ja existe'}, status=status.HTTP_400_BAD_REQUEST)
    #         except User.DoesNotExist:
    #             pass
