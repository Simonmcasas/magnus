from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    precio = models.FloatField()