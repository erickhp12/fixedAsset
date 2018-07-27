from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from marca.models import Marca

CIUDADES= (("Cd. Juarez", "Cd. Juarez"), ("Valle Hermoso", "Valle Hermoso"))

class Main(models.Model):
    user = models.ForeignKey(User, null=False, blank=False)
    pedimento = models.IntegerField(null=True, blank=True, unique=False, verbose_name=u'pedimento')
    numProyecto = models.CharField(max_length=200, null=True, blank=True, unique=True, verbose_name=u'Numero de proyecto')
    localizacion = models.CharField(max_length=200, null=True, blank=True, unique=False, verbose_name='Localizacion')
    ordenCompra = models.CharField(max_length=15, null=True, blank=True, unique=False, verbose_name=u'Orden de compra')
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=200,null=True, blank=True, unique=False, verbose_name=u'Modelo')
    serie = models.CharField(max_length=200, null=True, blank=True, unique=False, verbose_name=u'Serie')
    origen = models.CharField(choices=CIUDADES, max_length=200,null=True, blank=True,unique=False,verbose_name=u'Origen')
    precio = models.CharField(max_length=200, null=True, blank=True, unique=False, verbose_name=u'Precio')
    tipoCambio = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, unique=False, verbose_name=u'Tipo de cambio')
    fecha_ingreso = models.DateField(auto_now_add=False, verbose_name=u'fecha de ingreso')
    fecha_pedimento = models.DateField(auto_now_add=False, verbose_name=u'fecha de pedimento')
    descripcion = models.CharField(max_length=500, null=True, blank=True, unique=False, verbose_name=u'Descripcion')
    jssID = models.CharField(max_length=200, null=True, blank=True, unique=False, verbose_name=u'JSS ID')
    fecha_inicio = models.DateTimeField(auto_now_add=True, verbose_name=u'fecha_inicio')
    terminado = models.BooleanField(default=False)
    imagen = models.ImageField(null=True, blank=True, upload_to='main', verbose_name='Imagen')

    def save(self, force_insert=False, force_update=False, using=None):
        if self.pedimento is None:
            self.terminado = False
        else:
            self.terminado = True
        super(Main, self).save()

    @permalink
    def url_editar_main(self):
        return ('formularioMain', [int(self.pk)])
