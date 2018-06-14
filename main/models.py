from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from marca.models import Marca

class Main(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    pedimento = models.IntegerField( null=True, unique=False,verbose_name=u'pedimento')
    numProyecto = models.CharField(max_length=200, null=True, unique=False, verbose_name=u'Numero de proyecto')
    localizacion = models.CharField(max_length=200, null=True, unique=False, verbose_name='Localizacion')
    ordenCompra = models.CharField(max_length=15, null=True, unique=False, verbose_name=u'Orden de compra')
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=200,null=True,unique=False,verbose_name=u'Modelo')
    serie = models.CharField(max_length=200,null=True,unique=False,verbose_name=u'Serie')
    origen = models.CharField(max_length=200,null=True,unique=False,verbose_name=u'Origen')
    precio = models.CharField(max_length=200,null=True,unique=False,verbose_name=u'Precio')
    tipoCambio = models.DecimalField(max_digits=6, decimal_places=2,null=True,unique=False,verbose_name=u'Tipo de cambio')
    fecha_ingreso = models.DateTimeField(auto_now_add=False, verbose_name=u'fecha de ingreso')
    fecha_pedimento = models.DateTimeField(auto_now_add=False, verbose_name=u'fecha de pedimento')
    descripcion = models.CharField(max_length=500,null=True,unique=False,verbose_name=u'Descripcion')
    jssID = models.CharField(max_length=200,null=True,unique=False,verbose_name=u'JSS ID')
    fecha_inicio = models.DateTimeField(auto_now_add=True, verbose_name=u'fecha_inicio')

    @permalink
    def url_editar_main(self):
        return ('formularioMain', [int(self.pk)])
