# Generated by Django 3.1.4 on 2021-01-20 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0022_auto_20210118_1201'),
        ('certificaciones', '0015_criterio_clave'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='criterio',
            options={'ordering': ['pk_id', 'clave']},
        ),
        migrations.CreateModel(
            name='Certificacion',
            fields=[
                ('pk_id', models.OneToOneField(limit_choices_to={'fk_tipo': 4}, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='proyecto_cert', serialize=False, to='proyectos.proyecto')),
                ('criterios', models.ManyToManyField(through='certificaciones.CriterioProyecto', to='certificaciones.Criterio')),
            ],
        ),
        migrations.AlterField(
            model_name='criterioproyecto',
            name='fk_proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificaciones.certificacion'),
        ),
        migrations.DeleteModel(
            name='Proyecto',
        ),
    ]