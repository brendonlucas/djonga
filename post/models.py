from django.db import models

from usuario.models import Usuario


def upload_to_image(instance, filename):
    return 'images/{filename}'.format(filename=filename)


def upload_to_file(instance, filename):
    return 'file/{filename}'.format(filename=filename)


class Post(models.Model):
    title = models.CharField(max_length=100)
    descricao = models.CharField(max_length=250)
    foto = models.FileField(upload_to=upload_to_image, blank=True, null=True)
    # documento = models.FileField(upload_to=upload_to_file, blank=True, null=True)
    dono = models.ForeignKey(Usuario, on_delete=models.CASCADE, name='dono')
