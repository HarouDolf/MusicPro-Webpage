from django.db import models


# Create your models here.

class InstrumentoCuerdas(models.Model):
    serie_del_producto = models.CharField(max_length=6)
    marca = models.CharField(max_length=20)
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    tipo_de_producto = models.CharField(max_length=25)
    precio = models.CharField(max_length=10)

class Percusion(models.Model):
    serie_del_producto = models.CharField(max_length=6)
    marca = models.CharField(max_length=20)
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    tipo_de_producto = models.CharField(max_length=25)
    precio = models.CharField(max_length=10)

class Amplificadores(models.Model):
    serie_del_producto = models.CharField(max_length=6)
    marca = models.CharField(max_length=20)
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    tipo_de_producto = models.CharField(max_length=25)
    precio = models.CharField(max_length=10)

class AccesoriosVarios(models.Model):
    serie_del_producto = models.CharField(max_length=6)
    marca = models.CharField(max_length=20)
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    tipo_de_producto = models.CharField(max_length=25)
    precio = models.CharField(max_length=10)

class Venta(models.Model):
    precio_total = models.CharField(max_length=15)
    fecha =models.DateTimeField()



