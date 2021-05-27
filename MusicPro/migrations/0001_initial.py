# Generated by Django 3.2.2 on 2021-05-27 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=1000)),
                ('serie_del_producto', models.CharField(max_length=6)),
                ('marca', models.CharField(max_length=20)),
                ('codigo', models.CharField(max_length=50)),
                ('categoria_producto', models.CharField(choices=[('Instrumentos de cuerdas', 'Instrumentos de cuerdas'), ('Percusión', 'Percusión'), ('Amplificadores', 'Amplificadores'), ('Accesorios varios', 'Accesorios varios')], default='Instrumentos de cuerdas', max_length=30)),
                ('sub_categoria_producto', models.CharField(choices=[('No selection', 'No selection'), ('Guitarras', 'Guitarras'), ('Bajos', 'Bajos'), ('Pianos', 'Pianos'), ('Baterías acústicas', 'Baterías, acústicas'), ('Batería electrónica', 'Batería electrónica'), ('Cabezales', 'Cabezales'), ('Cajas', 'Cajas')], default='No selection', max_length=30)),
                ('sub_sub_categoria', models.CharField(choices=[('No selection', 'No selection'), ('Guitarras Cuerpo Solido', 'Guitarras Cuerpo Solido'), ('Guitarras Acústicas', 'Guitarras Acústicas'), ('Guitarras Eléctricas', 'Guitarras Eléctricas'), ('Bajos Cuatro Cuerdas', 'Bajos Cuatro Cuerdas'), ('Bajos Cinco Cuerdas', 'Bajos Cinco Cuerdas'), ('Bajos Activos', 'Bajos Activos'), ('Bajos Pasivos', 'Bajos Pasivos'), ('Piano de media cola', 'Piano de media cola'), ('Piano de cola entera', 'Piano de cola entera'), ('Pianolas', 'Pianolas')], default='No selection', max_length=30)),
                ('precio', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='instrumentos_images/', verbose_name='Imagen Principal')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_total', models.CharField(max_length=15)),
                ('fecha', models.DateTimeField()),
            ],
        ),
    ]
