from django.contrib import admin
from . import models as m

class MainAdmin(admin.ModelAdmin):
    list_display = ('pedimento',
                    'numProyecto',
                    'localizacion',
                    'ordenCompra',
                    'modelo',
                    'serie',
                    'origen',
                    'precio',
                    'tipoCambio',
                    'fecha_ingreso',
                    'fecha_pedimento',
                    'jssID',
                    'fecha_inicio')
    list_filter = ('pedimento','numProyecto')

    search_fields = ['pedimento',
                    'numProyecto',
                    'localizacion',
                    'ordenCompra',  
                    'modelo',
                    'serie',
                    'origen',
                    'precio',
                    'tipoCambio',
                    'fecha_ingreso',
                    'fecha_pedimento',
                    'jssID',
                    'fecha_inicio']

admin.site.register(m.Main, MainAdmin)