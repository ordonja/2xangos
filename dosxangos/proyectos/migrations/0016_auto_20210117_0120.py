# Generated by Django 3.1.4 on 2021-01-17 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0015_auto_20210117_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='fk_obs',
            field=models.ManyToManyField(blank=True, to='proyectos.Obs'),
        ),
    ]