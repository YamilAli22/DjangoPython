from django.contrib import admin
from .models import Pedido, LineaPedido

# Register your models here.
# para registrar modelos en el panel de administración
admin.site.register([Pedido, LineaPedido])
