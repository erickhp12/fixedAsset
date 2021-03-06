from django.contrib import admin
from . import models as m

class MarcaAdmin(admin.ModelAdmin):
    list_display = ( 'nombre','observaciones','fecha_inicio' )
    list_filter = ( 'nombre','observaciones' )

    search_fields = ['nombre','observaciones','fecha_inicio']

admin.site.register(m.Marca, MarcaAdmin)