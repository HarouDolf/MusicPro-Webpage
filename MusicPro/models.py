from django.db import models

# Create your models here.

INSTRUMENTOSDECUERDAS = 'Instrumentos de cuerdas'
PERCUSION = 'Percusión'
AMPLIFICADORES = 'Amplificadores'
ACCESORIOSVARIOS = 'Accesorios varios'
CATEGORIA_CHOICES = (
    (INSTRUMENTOSDECUERDAS, 'Instrumentos de cuerdas'),
    (PERCUSION, 'Percusión'),
    (AMPLIFICADORES, 'Amplificadores'),
    (ACCESORIOSVARIOS, 'Accesorios varios')
)

GUITARRAS = 'Guitarras'
BAJOS = 'Bajos'
PIANOS = 'Pianos'
BATERIASACUSTICAS = 'Baterías acústicas'
BATERIAELECTRONICA = 'Batería electrónica'
CABEZALES = 'Cabezales'
CAJAS = 'Cajas'
SUBCATEGORIA_CHOICES = (
    ('', '----------')
    (GUITARRAS, 'Guitarras'),
    (BAJOS, 'Bajos'),
    (PIANOS, 'Pianos'),
    (BATERIASACUSTICAS, 'Baterías, acústicas'),
    (BATERIAELECTRONICA, 'Batería electrónica'),
    (CABEZALES, 'Cabezales'),
    (CAJAS, 'Cajas')
)

GUITARRASCUERPOSOLIDO = 'Guitarras Cuerpo Solido'
GUITARRASACUSTICAS = 'Guitarras Acústicas'
GUITARRASELECTRICAS = 'Guitarras Eléctricas'
BAJOSCUATROCUERDAS = 'Bajos Cuatro Cuerdas'
BAJOSCINCOCUERDAS = 'Bajos Cinco Cuerdas'
BAJOSACTIVOS = 'Bajos Activos'
BAJOSPASIVOS = 'Bajos Pasivos'
PIANODEMEDIACOLA = 'Piano de media cola'
PIANODECOLAENTERA = 'Piano de cola entera'
PIANOLAS = 'Pianolas'
SUBSUBCATEGORIA_CHOICES = (
    ('','----------'),
    (GUITARRASCUERPOSOLIDO, 'Guitarras Cuerpo Solido'),
    (GUITARRASACUSTICAS, 'Guitarras Acústicas'),
    (GUITARRASELECTRICAS, 'Guitarras Eléctricas'),
    (BAJOSCUATROCUERDAS, 'Bajos Cuatro Cuerdas'),
    (BAJOSCINCOCUERDAS, 'Bajos Cinco Cuerdas'),
    (BAJOSACTIVOS, 'Bajos Activos'),
    (BAJOSPASIVOS, 'Bajos Pasivos'),
    (PIANODEMEDIACOLA, 'Piano de media cola'),
    (PIANODECOLAENTERA, 'Piano de cola entera'),
    (PIANOLAS, 'Pianolas')
)


class Productos(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=1000)
    serie_del_producto = models.CharField(max_length=6)
    marca = models.CharField(max_length=20)
    codigo = models.CharField(max_length=50)
    categoria_producto = models.CharField(max_length=30, choices=CATEGORIA_CHOICES, default=INSTRUMENTOSDECUERDAS)
    sub_categoria_producto = models.CharField(max_length=30, choices=SUBCATEGORIA_CHOICES, default='')
    sub_sub_categoria = models.CharField(max_length=30, choices=SUBSUBCATEGORIA_CHOICES,default='')
    precio = models.CharField(max_length=10)
    image = models.ImageField(upload_to='instrumentos_images/', verbose_name='Imagen Principal')


class Venta(models.Model):
    precio_total = models.CharField(max_length=15)
    fecha = models.DateTimeField()
