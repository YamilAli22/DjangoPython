from django.contrib import admin
from .models import CategoriaProducto, Producto

# Register your models here.
# para registrar modelos en el panel de administración

class CategoriaProdAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(CategoriaProducto, CategoriaProdAdmin)
admin.site.register(Producto, ProductoAdmin)