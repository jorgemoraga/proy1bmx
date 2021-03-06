# Generated by Django 3.1.5 on 2021-01-19 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bicicleta',
            fields=[
                ('idBicicleta', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='ID Bicicleta')),
                ('marca', models.CharField(max_length=20, verbose_name='Marca de la Bicicleta')),
                ('modelo', models.CharField(blank=True, max_length=20, null=True, verbose_name='Modelo')),
                ('color', models.CharField(blank=True, max_length=20, null=True, verbose_name='Color')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.categoria')),
            ],
        ),
        migrations.DeleteModel(
            name='Vehiculo',
        ),
    ]
