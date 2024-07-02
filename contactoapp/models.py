from django.db import models

# Create your models here.
class Contacto(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    
    class Meta:
        verbose_name = "Contacto"
        ordering = ['name']

    def __str__(self):
        return self.name
