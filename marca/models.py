from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User 

class Marca(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    nombre = models.CharField(max_length=50, null=True, unique=False, verbose_name='Nombre')
    observaciones = models.CharField(max_length=200, null=True, unique=False, verbose_name=u'Observaciones')
    fecha_inicio = models.DateTimeField(auto_now_add=True, verbose_name=u'fecha_inicio')

    def __str__(self):
        return self.nombre

    @permalink
    def url_editar_marca(self):
        return ('formulario', [int(self.pk)])
