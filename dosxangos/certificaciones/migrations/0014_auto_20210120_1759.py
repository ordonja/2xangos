# Generated by Django 3.1.4 on 2021-01-20 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificaciones', '0013_indicador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='criterio',
            name='indicador',
        ),
        migrations.AddField(
            model_name='criterio',
            name='indicadores',
            field=models.ManyToManyField(blank=True, related_name='criterio_ind', to='certificaciones.Indicador'),
        ),
    ]