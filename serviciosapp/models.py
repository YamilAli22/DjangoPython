from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='serviciosapp')
    created = models.DateTimeField(auto_now_add=True) # PARA QUE AGREGE LA FECHA DE FORMA AUTOMATICA
    updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo
    
    
    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
    
