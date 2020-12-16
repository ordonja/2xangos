# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Equipo(models.Model):
    pk_id = models.AutoField(primary_key=True)
    fk_equipotipo = models.ForeignKey('Tipoequipo', models.DO_NOTHING, db_column='fk_equipoTipo', blank=True, null=True)  # Field name made lowercase.
    marca = models.TextField(blank=True, null=True)
    modelo = models.TextField(blank=True, null=True)
    serial = models.TextField(blank=True, null=True)
    fk_paisorigen = models.ForeignKey('directorio.Pais', on_delete= models.SET_NULL, verbose_name="pais",
        related_name="equipos", db_column='fk_paisOrigen', blank=True, null=True)  # Field name made lowercase.
    fichatécnica = models.TextField(db_column='fichaTécnica', blank=True, null=True)  # Field name made lowercase.
    url_ft = models.TextField(blank=True, null=True)  # This field type is a guess.
    anhofabricacion = models.IntegerField(db_column='anhoFabricacion', blank=True, null=True)  # Field name made lowercase.
    capacidad = models.FloatField(blank=True, null=True)
    fk_unidadcapacidad = models.ForeignKey('Unidadmedicion', on_delete= models.SET_NULL,
        db_column='fk_unidadCapacidad', blank=True, null=True, related_name="eq_capacidad")  # Field name made lowercase.
    potencia = models.FloatField(blank=True, null=True)
    fk_unidadpotencia = models.ForeignKey('Unidadmedicion', on_delete= models.SET_NULL,
        db_column='fk_unidadPotencia', blank=True, null=True, related_name="eq_potencia")  # Field name made lowercase.
    consumoener = models.FloatField(db_column='consumoEner', blank=True, null=True)  # Field name made lowercase.
    fk_unidadener = models.ForeignKey('Unidadmedicion', on_delete= models.SET_NULL,
        db_column='fk_unidadEner', blank=True, null=True, related_name="eq_energia")  # Field name made lowercase.
    fuenteener = models.TextField(db_column='fuenteEner', blank=True, null=True)  # Field name made lowercase.
    fk_equipopadre = models.ForeignKey('self', on_delete= models.SET_NULL, db_column='fk_equipoPadre', blank=True, null=True)  # Field name made lowercase.
    fk_obs = models.ForeignKey('proyecto.Obs', on_delete= models.SET_NULL, db_column='fk_obs', blank=True, null=True)
    stamp_creacion = models.DateTimeField(blank=True, null=True)
    stamp_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipo'


class Tipoequipo(models.Model):
    tipo = models.TextField(blank=True, null=True)
    fk_norma = models.IntegerField(blank=True, null=True)
    fk_supertipo = models.ForeignKey('self', on_delete= models.SET_NULL, db_column='fk_supertipo', blank=True, null=True)
    pk_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'tipoEquipo'


class Unidadmedicion(models.Model):
    pk_id = models.AutoField(primary_key=True)
    sistema = models.TextField(blank=True, null=True)
    unidad = models.TextField(blank=True, null=True)
    simbolo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unidadMedicion'
