# Generated by Django 4.0 on 2021-12-31 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='services_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titlo', models.CharField(max_length=30)),
                ('contenido', models.CharField(max_length=500)),
                ('imagen', models.ImageField(upload_to='')),
                ('fecha_de_creacion', models.DateTimeField(auto_now=True)),
                ('ultima_actualizacion', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
