# Generated by Django 3.2.2 on 2021-05-28 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MusicPro', '0002_delete_venta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=30)),
            ],
        ),
    ]
