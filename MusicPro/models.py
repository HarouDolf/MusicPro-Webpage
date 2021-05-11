from django.db import models


# Create your models here.

class Guitarras(models.Model):
    serie_del_producto = models.CharField(max_length=6)
    marca = models.CharField(max_length=20)
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    tipo_de_producto = models.CharField(max_length=25)
    precio = models.CharField(max_length=10)


class Bajos(models.Model):
    serie_del_producto = models.CharField(max_length=6)
    marca = models.CharField(max_length=20)
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    tipo_de_producto = models.CharField(max_length=25)
    precio = models.CharField(max_length=10)


class Pianos(models.Model):
    serie_del_producto = models.CharField(max_length=6)
    marca = models.CharField(max_length=20)
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    tipo_de_producto = models.CharField(max_length=25)
    precio = models.CharField(max_length=10)


class BateriasAcusticas(models.Model):
    serie_del_producto = models.CharField(max_length=6)
    marca = models.CharField(max_length=20)
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    tipo_de_producto = models.CharField(max_length=25)
    precio = models.CharField(max_length=10)


class BateriasElectronica(models.Model):
    serie_del_producto = models.CharField(max_length=6)
    marca = models.CharField(max_length=20)
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    tipo_de_producto = models.CharField(max_length=25)
    precio = models.CharField(max_length=10)


class Cabezales(models.Model):
    serie_del_producto = models.CharField(max_length=6)
    marca = models.CharField(max_length=20)
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    tipo_de_producto = models.CharField(max_length=25)
    precio = models.CharField(max_length=10)


class Cajas(models.Model):
    serie_del_producto = models.CharField(max_length=6)
    marca = models.CharField(max_length=20)
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    tipo_de_producto = models.CharField(max_length=25)
    precio = models.CharField(max_length=10)


class Audifonos(models.Model):
    serie_del_producto = models.CharField(max_length=6)
    marca = models.CharField(max_length=20)
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=25)
    precio = models.CharField(max_length=10)


class Monitores(models.Model):
    serie_del_producto = models.CharField(max_length=6)
    marca = models.CharField(max_length=20)
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=25)
    precio = models.CharField(max_length=10)


class Parlantes(models.Model):
    serie_del_producto = models.CharField(max_length=6)
    marca = models.CharField(max_length=20)
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=25)
    precio = models.CharField(max_length=10)


class Cables(models.Model):
    serie_del_producto = models.CharField(max_length=6)
    marca = models.CharField(max_length=20)
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=25)
    precio = models.CharField(max_length=10)


class Microfonos(models.Model):
    serie_del_producto = models.CharField(max_length=6)
    marca = models.CharField(max_length=20)
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=25)
    precio = models.CharField(max_length=10)


class Interfaces(models.Model):
    serie_del_producto = models.CharField(max_length=6)
    marca = models.CharField(max_length=20)
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=25)
    precio = models.CharField(max_length=10)


class Mixers(models.Model):
    serie_del_producto = models.CharField(max_length=6)
    marca = models.CharField(max_length=20)
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=25)
    precio = models.CharField(max_length=10)
