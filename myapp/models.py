from django.db import models

# Create your models here.
#productos_y_producciones
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre