# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Pais(models.Model):
    pk_id = models.AutoField(primary_key=True)
    cod = models.CharField(max_length=3, blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)
    nombreoficial = models.TextField(db_column='nombreOficial', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pais'

class Estado(models.Model):
    pk_id = models.AutoField(primary_key=True)
    cod = models.CharField(max_length=3, blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)
    nombreoficial = models.TextField(db_column='nombreOficial', blank=True, null=True)  # Field name made lowercase.
    fk_pais = models.ForeignKey('Pais', models.DO_NOTHING, db_column='fk_pais', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado'

class Companhia(models.Model):
    pk_id = models.AutoField(primary_key=True)
    razonsocial = models.TextField(db_column='razonSocial', blank=True, null=True)  # Field name made lowercase.
    nombre = models.TextField(blank=True, null=True)
    rfc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'companhia'

class Persona(models.Model):
    pk_id = models.AutoField(primary_key=True)
    nombres = models.TextField(blank=True, null=True)
    apellidos = models.TextField(blank=True, null=True)
    razonsocial = models.TextField(db_column='razonSocial', blank=True, null=True)  # Field name made lowercase.
    rfc = models.TextField(blank=True, null=True)
    clave = models.CharField(max_length=4, blank=True, null=True)
    fk_titulo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persona'


class Direccion(models.Model):
    pk_id = models.AutoField(primary_key=True)
    cp = models.TextField(blank=True, null=True)
    calle = models.TextField(blank=True, null=True)
    numero = models.TextField(blank=True, null=True)
    colonia = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    fk_estado = models.ForeignKey('Estado', models.DO_NOTHING, db_column='fk_estado', blank=True, null=True)
    codigoplus = models.TextField(db_column='codigoPlus', blank=True, null=True)  # Field name made lowercase.
    utmx = models.FloatField(blank=True, null=True)
    utmy = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direccion'
