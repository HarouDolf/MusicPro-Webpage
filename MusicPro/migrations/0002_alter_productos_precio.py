# Generated by Django 3.2.2 on 2021-06-28 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MusicPro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='precio',
            field=models.IntegerField(default=0, null=True),
        ),
    ]