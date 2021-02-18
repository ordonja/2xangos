# Generated by Django 3.1.4 on 2021-02-16 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0003_auto_20210216_1657'),
    ]

    operations = [
        migrations.RenameField(
            model_name='normaequipo',
            old_name='fk_normal',
            new_name='fk_norma',
        ),
        migrations.AlterField(
            model_name='unidadmedicion',
            name='sistema',
            field=models.TextField(blank=True, choices=[('0', 'SI'), ('1', 'BU')], null=True),
        ),
    ]
