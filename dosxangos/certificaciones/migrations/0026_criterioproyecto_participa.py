#Generated by Django 3.1.4 on 2021-02-23-03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificaciones', '0025_auto_20210123_0105'),
    ]

    operations = [
        migrations.AddField(
            model_name='criterioproyecto',
            name='participa',
            field=models.BooleanField(blank=True, null=True),
        )
    ]
