from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Usuario(models.Model):
    nome = models.CharField(max_length=250)
    telefone = models.IntegerField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
