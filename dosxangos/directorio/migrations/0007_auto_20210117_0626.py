# Generated by Django 3.1.4 on 2021-01-17 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directorio', '0006_auto_20210117_0121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companhia',
            old_name='razonsocial',
            new_name='razon_social',
        ),
        migrations.RenameField(
            model_name='estado',
            old_name='cod',
            new_name='clave',
        ),
        migrations.RenameField(
            model_name='estado',
            old_name='nombreoficial',
            new_name='nombre_oficial',
        ),
        migrations.RenameField(
            model_name='pais',
            old_name='cod',
            new_name='clave',
        ),
        migrations.RenameField(
            model_name='pais',
            old_name='nombreoficial',
            new_name='nombre_oficial',
        ),
        migrations.AddField(
            model_name='direccion',
            name='estado',
            field=models.ForeignKey(blank=True, db_column='fk_estado', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='directorio.estado'),
        ),
        migrations.AddField(
            model_name='estado',
            name='fk_pais',
            field=models.ForeignKey(blank=True, db_column='fk_pais', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='directorio.pais'),
        ),
    ]
