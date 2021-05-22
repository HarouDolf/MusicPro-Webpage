from django.contrib import admin
from .models import Productos, Venta

# Register your models here.

admin.site.site_header = "Administración MusicPro"
admin.site.site_title = "Administracion"
admin.site.index_title = "Portal de ingreso/modificacion de productos"

class productoAdmin(admin.ModelAdmin):
  list_display = ('categoria_producto','nombre', 'marca', 'precio')

admin.site.register(Productos,productoAdmin)

class ventaAdmin(admin.ModelAdmin):
  list_display = ('precio_total','fecha')

admin.site.register(Venta,ventaAdmin)
