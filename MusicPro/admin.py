from django.contrib import admin
from .models import Productos, Categoria, Subcategoriacuerdas

# Register your models here.

admin.site.site_header = "Administración MusicPro"
admin.site.site_title = "Administracion"
admin.site.index_title = "Portal de ingreso/modificacion de productos"

class productoAdmin(admin.ModelAdmin):
  list_display = ('categoria_producto','nombre', 'marca', 'precio')

class categoriaAdmin(admin.ModelAdmin):
  list_display = ('pk','categoria')

class subcategoriacuerdasAdmin(admin.ModelAdmin):
  list_display = ('pk','subcategoriacuerdas')

admin.site.register(Productos,productoAdmin)
admin.site.register(Categoria,categoriaAdmin)
admin.site.register(Subcategoriacuerdas,subcategoriacuerdasAdmin)