# Generated by Django 3.2.16 on 2022-12-22 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleProductos',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Marca', models.CharField(max_length=25)),
                ('Descripcion', models.TextField(max_length=250)),
                ('Modelo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='')),
                ('username', models.CharField(max_length=24, unique=True, verbose_name='')),
                ('photo', models.ImageField(default='media/ImagePerfil/userImageDefault.png', max_length=40, upload_to='media/ImagePerfil/', verbose_name='')),
                ('activo', models.BooleanField(default=True)),
                ('admin', models.BooleanField(default=False)),
                ('staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Valor', models.IntegerField()),
                ('Stock', models.IntegerField()),
                ('Ventas', models.IntegerField()),
                ('DetalleProductos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Principal.detalleproductos')),
            ],
        ),
    ]
