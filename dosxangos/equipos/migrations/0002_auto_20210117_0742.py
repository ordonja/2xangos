# Generated by Django 3.1.4 on 2021-01-17 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipo',
            old_name='pk_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='tipoequipo',
            old_name='pk_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='unidadmedicion',
            old_name='pk_id',
            new_name='id',
        ),
        migrations.AlterModelTable(
            name='equipo',
            table=None,
        ),
        migrations.AlterModelTable(
            name='tipoequipo',
            table=None,
        ),
        migrations.AlterModelTable(
            name='unidadmedicion',
            table=None,
        ),
    ]