from django.contrib import admin
from .models import InstrumentoCuerdas, Percusion, Amplificadores, AccesoriosVarios

# Register your models here.

class productoAdmin(admin.ModelAdmin):
  list_display = ('tipo_de_producto', 'nombre', 'marca', 'precio')

admin.site.register(InstrumentoCuerdas,productoAdmin)
admin.site.register(Percusion,productoAdmin)
admin.site.register(Amplificadores,productoAdmin)
admin.site.register(AccesoriosVarios,productoAdmin)
