from django.db import models
from django.db.models import permalink

class Marca(models.Model):
    id_marca = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=True, unique=False, verbose_name='Nombre')
    observaciones = models.CharField(max_length=200, null=True, unique=False, verbose_name=u'Observaciones')
    fecha_inicio = models.DateTimeField(auto_now_add=True, verbose_name=u'fecha_inicio')

    @permalink
    def url_editar_marca(self):
        return ('marca', [int(self.pk)])
