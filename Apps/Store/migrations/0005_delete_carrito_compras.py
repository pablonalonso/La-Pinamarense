# Generated by Django 4.0.1 on 2022-01-13 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0004_alter_carrito_compras_cliente'),
    ]

    operations = [
        migrations.DeleteModel(
            name='carrito_compras',
        ),
    ]