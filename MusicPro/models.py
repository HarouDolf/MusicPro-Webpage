from django.db import models


# Create your models here.

class Productos(models.Model):
    serie_del_producto = models.CharField(max_length=6)
    marca = models.CharField(max_length=20)
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    categoria_producto = models.CharField(max_length=25)
    sub_categoria_producto = models.CharField(max_length=25)
    precio = models.CharField(max_length=10)
    image = models.ImageField(upload_to='instrumentos_images/', verbose_name='Imagen Principal')

class Venta(models.Model):
    precio_total = models.CharField(max_length=15)
    fecha =models.DateTimeField()



