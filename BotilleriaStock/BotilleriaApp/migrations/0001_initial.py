# Generated by Django 5.0.6 on 2024-06-17 19:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('nombre_usuario', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=254)),
                ('rut', models.CharField(max_length=12, primary_key=True, serialize=False, unique=True)),
                ('numero_documento', models.CharField(max_length=6)),
                ('contraseña', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('sku', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=60)),
                ('precio', models.PositiveIntegerField()),
                ('cantidad', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.JSONField()),
                ('total', models.PositiveIntegerField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BotilleriaApp.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('S', 'Salida'), ('E', 'Entrada')], max_length=1)),
                ('cantidad', models.PositiveIntegerField()),
                ('fecha_movimiento', models.DateTimeField(auto_now_add=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BotilleriaApp.producto')),
            ],
        ),
    ]
