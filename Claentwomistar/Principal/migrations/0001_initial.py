# Generated by Django 3.2.16 on 2022-12-21 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
    ]
