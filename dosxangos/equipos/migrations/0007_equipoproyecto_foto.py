# Generated by Django 3.1.4 on 2021-02-16 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0006_auto_20210216_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipoproyecto',
            name='foto',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
    ]
