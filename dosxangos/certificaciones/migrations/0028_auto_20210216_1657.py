# Generated by Django 3.1.4 on 2021-02-16 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('certificaciones', '0027_auto_20210125_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criterioproyecto',
            name='fk_criterio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificaciones.criterio'),
        ),
    ]