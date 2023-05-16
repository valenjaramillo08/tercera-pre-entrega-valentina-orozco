from django.db import models

# Create your models here.
class familia(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    telefono = models.IntegerField()
    nacimiento = models.DateTimeField()
