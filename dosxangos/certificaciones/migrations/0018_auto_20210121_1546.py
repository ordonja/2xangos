# Generated by Django 3.1.4 on 2021-01-21 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificaciones', '0017_auto_20210121_1542'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='criterio',
            options={'ordering': ['id', 'clave']},
        ),
        migrations.RenameField(
            model_name='criterio',
            old_name='pk_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='criterioproyecto',
            old_name='pk_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='evidenciacriterio',
            old_name='pk_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='evidenciareq',
            old_name='pk_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='rubro',
            old_name='pk_id',
            new_name='id',
        ),
    ]