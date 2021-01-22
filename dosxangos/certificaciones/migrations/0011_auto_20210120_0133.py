# Generated by Django 3.1.4 on 2021-01-20 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificaciones', '0010_auto_20210120_0054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('aplica_dc', models.BooleanField(blank=True, null=True)),
                ('aplica_op', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='criterio',
            name='meta',
        ),
        migrations.AddField(
            model_name='criterio',
            name='metas',
            field=models.ManyToManyField(blank=True, null=True, to='certificaciones.Meta'),
        ),
    ]
