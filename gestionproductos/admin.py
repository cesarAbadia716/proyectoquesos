from django.contrib import admin
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('proveedor', 'cantidad', 'precio_compra', 'fecha', 'calidad', 'usuario_modificacion')
    list_filter = ('proveedor', 'fecha')
    search_fields = ('proveedor__nombre', 'calidad')
    date_hierarchy = 'fecha'

admin.site.register(Producto, ProductoAdmin)
