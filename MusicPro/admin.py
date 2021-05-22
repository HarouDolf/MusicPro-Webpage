from django.contrib import admin
from .models import InstrumentoCuerdas, Percusion, Amplificadores, AccesoriosVarios

# Register your models here.

admin.site.site_header = "Administración MusicPro"
admin.site.site_title = "Administracion"
admin.site.index_title = "Portal de ingreso/modificacion de productos"

class productoAdmin(admin.ModelAdmin):
  list_display = ('tipo_de_producto', 'nombre', 'marca', 'precio')

admin.site.register(InstrumentoCuerdas,productoAdmin)
admin.site.register(Percusion,productoAdmin)
admin.site.register(Amplificadores,productoAdmin)
admin.site.register(AccesoriosVarios,productoAdmin)
