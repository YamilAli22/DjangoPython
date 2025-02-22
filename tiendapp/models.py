from django.db import models

# Create your models here.

class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "categoriaProd"
        verbose_name_plural = "categoriasProd"
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    categorias = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE) # clave foranea
                                                                                # para relacionar
                                                                                # la clase Producto con CategoriaProducto
    precio = models.FloatField()
    imagen = models.ImageField(upload_to="tienda", null=True, blank=True)       
    disponibilidad = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
    
