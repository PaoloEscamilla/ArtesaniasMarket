# Generated by Django 5.1.3 on 2024-12-05 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_alter_carritoproducto_cantidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='cantidad_disponible',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='vendedor',
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='productos/'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
