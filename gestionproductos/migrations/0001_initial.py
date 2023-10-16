# Generated by Django 4.2.6 on 2023-10-14 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=10)),
                ('precio_compra', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha', models.DateField()),
                ('calidad', models.CharField(max_length=100)),
                ('datos_fisicoquimicos', models.TextField()),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionproductos.proveedor')),
            ],
        ),
    ]
