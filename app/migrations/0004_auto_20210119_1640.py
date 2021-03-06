# Generated by Django 3.1 on 2021-01-19 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210119_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='bicicleta',
            name='color',
            field=models.CharField(max_length=20, null=True, verbose_name='Color'),
        ),
        migrations.AddField(
            model_name='bicicleta',
            name='imagen',
            field=models.ImageField(null=True, upload_to='bicicletas'),
        ),
        migrations.AddField(
            model_name='bicicleta',
            name='modelo',
            field=models.CharField(max_length=20, null=True, verbose_name='modelo'),
        ),
        migrations.AlterField(
            model_name='bicicleta',
            name='precio',
            field=models.IntegerField(blank=True, null=True, verbose_name='Precio'),
        ),
    ]
