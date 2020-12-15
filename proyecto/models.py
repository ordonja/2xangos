# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Areasproy(models.Model):
    pk = models.AutoField(primary_key=True)
    fk_proy = models.IntegerField(blank=True, null=True)
    supconstsnb = models.FloatField(db_column='supConstSNB', blank=True, null=True)  # Field name made lowercase.
    supconstbnb = models.FloatField(db_column='supConstBNB', blank=True, null=True)  # Field name made lowercase.
    supdesplante = models.FloatField(db_column='supDesplante', blank=True, null=True)  # Field name made lowercase.
    suppavimentos = models.FloatField(db_column='supPavimentos', blank=True, null=True)  # Field name made lowercase.
    supverdeperm = models.FloatField(db_column='supVerdePerm', blank=True, null=True)  # Field name made lowercase.
    supverdeimper = models.FloatField(db_column='supVerdeImper', blank=True, null=True)  # Field name made lowercase.
    supotraslibres = models.FloatField(db_column='supOtrasLibres', blank=True, null=True)  # Field name made lowercase.
    version = models.TextField(blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)
    fk_proyecto = models.IntegerField(blank=True, null=True)
    fk_obs = models.IntegerField(blank=True, null=True)
    stampcrea = models.DateTimeField(db_column='stampCrea', blank=True, null=True)  # Field name made lowercase.
    stampmod = models.DateTimeField(db_column='stampMod', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'areasProy'


class Equipo(models.Model):
    pk_equipo = models.AutoField(primary_key=True)
    fk_equipotipo = models.IntegerField(db_column='fk_equipoTipo', blank=True, null=True)  # Field name made lowercase.
    marca = models.TextField(blank=True, null=True)
    modelo = models.TextField(blank=True, null=True)
    serial = models.TextField(blank=True, null=True)
    fk_paisorigen = models.IntegerField(db_column='fk_paisOrigen', blank=True, null=True)  # Field name made lowercase.
    fichatécnica = models.TextField(db_column='fichaTécnica', blank=True, null=True)  # Field name made lowercase.
    url_ft = models.TextField(blank=True, null=True)  # This field type is a guess.
    anhofabricacion = models.IntegerField(db_column='anhoFabricacion', blank=True, null=True)  # Field name made lowercase.
    capacidad = models.FloatField(blank=True, null=True)
    fk_unidadcapacidad = models.IntegerField(db_column='fk_unidadCapacidad', blank=True, null=True)  # Field name made lowercase.
    potencia = models.FloatField(blank=True, null=True)
    fk_unidadpotencia = models.IntegerField(db_column='fk_unidadPotencia', blank=True, null=True)  # Field name made lowercase.
    consumoener = models.FloatField(db_column='consumoEner', blank=True, null=True)  # Field name made lowercase.
    fk_unidadener = models.IntegerField(db_column='fk_unidadEner', blank=True, null=True)  # Field name made lowercase.
    fuenteener = models.TextField(db_column='fuenteEner', blank=True, null=True)  # Field name made lowercase.
    fk_equipopadre = models.IntegerField(db_column='fk_equipoPadre', blank=True, null=True)  # Field name made lowercase.
    fk_obs = models.IntegerField(blank=True, null=True)
    stamp_creacion = models.DateTimeField(blank=True, null=True)
    stamp_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipo'


class Espacio(models.Model):
    pk_espacio = models.AutoField(primary_key=True)
    nombre = models.TextField(blank=True, null=True)
    sup = models.FloatField(blank=True, null=True)
    nivel = models.TextField(blank=True, null=True)
    tipo = models.TextField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    supdesp = models.FloatField(db_column='supDesp', blank=True, null=True)  # Field name made lowercase.
    supconst = models.FloatField(db_column='supConst', blank=True, null=True)  # Field name made lowercase.
    alturasnb = models.FloatField(db_column='alturaSNB', blank=True, null=True)  # Field name made lowercase.
    fk_obs = models.IntegerField(blank=True, null=True)
    fk_proyecto = models.IntegerField(blank=True, null=True)
    kf_espaciopadre = models.IntegerField(db_column='kf_espacioPadre', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'espacio'


class Obs(models.Model):
    pk = models.AutoField(primary_key=True)
    obs = models.TextField(blank=True, null=True)
    stampcrea = models.DateTimeField(db_column='stampCrea', blank=True, null=True)  # Field name made lowercase.
    stampmod = models.DateTimeField(db_column='stampMod', blank=True, null=True)  # Field name made lowercase.
    fk_creador = models.IntegerField(blank=True, null=True)
    fk_modif = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'obs'


class Predio(models.Model):
    pk = models.AutoField(primary_key=True)
    nombre = models.TextField(blank=True, null=True)
    sup = models.FloatField(blank=True, null=True)
    fk_direccion = models.IntegerField(blank=True, null=True)
    zonificacion = models.TextField(blank=True, null=True)
    ctacatastro = models.TextField(db_column='ctaCatastro', blank=True, null=True)  # Field name made lowercase.
    fk_obs = models.IntegerField(blank=True, null=True)
    fk_prediopadre = models.IntegerField(db_column='fk_predioPadre', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'predio'


class Proyecto(models.Model):
    pk_id = models.AutoField(primary_key=True)
    nombre = models.TextField(blank=True, null=True)
    tipo = models.TextField(blank=True, null=True)
    cliente = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    fechainicio = models.DateField(db_column='fechaInicio', blank=True, null=True)  # Field name made lowercase.
    fechafin = models.DateField(db_column='fechaFin', blank=True, null=True)  # Field name made lowercase.
    estado = models.TextField(blank=True, null=True)
    avance = models.FloatField(blank=True, null=True)
    fk_proyectopadre = models.IntegerField(db_column='fk_proyectoPadre', blank=True, null=True)  # Field name made lowercase.
    fk_predio = models.IntegerField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    stampcrea = models.DateTimeField(db_column='stampCrea', blank=True, null=True)  # Field name made lowercase.
    stampmod = models.DateTimeField(db_column='stampMod', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proyecto'


class Tipoequipo(models.Model):
    tipo = models.TextField(blank=True, null=True)
    fk_norma = models.IntegerField(blank=True, null=True)
    fk_supertipo = models.IntegerField(blank=True, null=True)
    pk = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'tipoEquipo'


class Unidadmedicion(models.Model):
    pk = models.AutoField(primary_key=True)
    sistema = models.TextField(blank=True, null=True)
    unidad = models.TextField(blank=True, null=True)
    simbolo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unidadMedicion'
