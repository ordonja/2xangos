# Generated by Django 3.1.4 on 2021-01-21 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('espacios', '0008_auto_20210118_1206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='espacio',
            old_name='pk_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='superficie',
            old_name='pk_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='zonificacion',
            old_name='pk_id',
            new_name='id',
        ),
    ]