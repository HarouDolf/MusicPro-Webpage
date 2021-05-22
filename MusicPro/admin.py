from django.contrib import admin
from .models import Productos, Venta

# Register your models here.

class productoAdmin(admin.ModelAdmin):
  list_display = ('categoria_producto','nombre', 'marca', 'precio')

admin.site.register(Productos,productoAdmin)

class ventaAdmin(admin.ModelAdmin):
  list_display = ('precio_total','fecha')

admin.site.register(Venta,ventaAdmin)
