from django.contrib import admin
from .models import Servicio

# Register your models here.
# para registrar modelos en el panel de administración

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Servicio, ServicioAdmin)


