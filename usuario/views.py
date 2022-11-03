from rest_framework.authtoken.models import Token

from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from usuario.models import *
from usuario.serializers import *


class UserList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = FuncionarioSerializer
    name = 'Funcionario-list'
    # permission_classes = (permissions.IsAuthenticated,)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = FuncionarioSerializer
    name = 'Funcionario-detail'
    # permission_classes = (permissions.IsAuthenticated,)




class UserAdd(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = AddUserSerializer
    name = 'Add-Funcionario'

    # permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        data = AddUserSerializer(data=request.data)
        if data.is_valid():
            print(data['user']['username'].value)
            print(data['user']['password'].value)
            print(data['user']['email'].value)
            print()
            print()
            user = User.objects.create_user(username=data['user']['username'].value,
                                            password=data['user']['password'].value,
                                            email=data['user']['email'].value)
            funcionario = Usuario(nome=data['nome'].value, telefone=data['telefone'].value, user=user)
            funcionario.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        else:
            try:
                user = User.objects.get(username=data['user']['username'].value)
                if user:
                    return Response({'error': 'usuario ja existe'}, status=status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist:
                pass


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        dados_funcionario = get_object_or_404(Usuario, user=user.id)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'nome': dados_funcionario.nome
        })
