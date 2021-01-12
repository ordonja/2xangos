# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

TIPO_ESPACIO_CHOICES = [
('gn', 'Genérico'),
('pr', 'Predio'),
('ed', 'Edificio'),
('ps', 'Piso'),
]

class Espacio(models.Model):
    pk_id = models.AutoField(primary_key=True)
    nombre = models.TextField(blank=True, null=True)
    sup = models.FloatField(blank=True, null=True)
    nivel = models.TextField(blank=True, null=True)
    tipo = models.TextField(max_length=2, default='gn', choices=TIPO_ESPACIO_CHOICES,)
    estado = models.TextField(blank=True, null=True)
    supdesp = models.FloatField(db_column='supDesp', blank=True, null=True)  # Field name made lowercase.
    supconst = models.FloatField(db_column='supConst', blank=True, null=True)  # Field name made lowercase.
    alturasnb = models.FloatField(db_column='alturaSNB', blank=True, null=True)  # Field name made lowercase.

    fk_obs = models.ForeignKey('proyectos.Obs', models.CASCADE, db_column='fk_obs', blank=True, null=True)
    fk_proyecto = models.ForeignKey('proyectos.Proyecto', models.SET_NULL, db_column='fk_proyecto', blank=True, null=True)
    fk_espaciopadre = models.ForeignKey('self', models.SET_NULL, db_column='fk_espacioPadre', blank=True, null=True)  # Field name made lowercase.

    #equipos = models.ManyToManyField('')
    class Meta:
        managed = False
        db_table = 'espacios'

class Instalacion:
    pk_id = models.AutoField(primary_key=True)
    nombre = models.TextField(blank=True, null=True)
