# Generated by Django 4.2.3 on 2023-07-16 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, default=None),
        ),
    ]
