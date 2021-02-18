# Generated by Django 3.1.4 on 2021-02-16 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0005_auto_20210216_1819'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipoproyecto',
            old_name='fk_equipo',
            new_name='equipo',
        ),
        migrations.RenameField(
            model_name='equipoproyecto',
            old_name='fk_proyecto',
            new_name='proyecto',
        ),
        migrations.RemoveField(
            model_name='equipo',
            name='serial',
        ),
        migrations.AddField(
            model_name='equipoproyecto',
            name='cantidad',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='equipoproyecto',
            name='serial',
            field=models.TextField(blank=True, null=True),
        ),
    ]
