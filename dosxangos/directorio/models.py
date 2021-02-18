# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

class Pais(models.Model):
    id = models.AutoField(primary_key=True)
    clave = models.CharField(max_length=3)
    nombre = models.TextField(blank=True, null=True)
    nombre_oficial = models.TextField(db_column='nombreOficial', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'pais'

    def __str__(self):
        return(self.clave)


class Estado(models.Model):
    id = models.AutoField(primary_key=True)
    clave = models.CharField(max_length=3, blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)
    nombre_oficial = models.TextField(db_column='nombreOficial', blank=True, null=True)  # Field name made lowercase.
    fk_pais = models.ForeignKey('Pais', models.DO_NOTHING, db_column='fk_pais', blank=True, null=True)

    class Meta:
        db_table = 'estado'

    def __str__(self):
        if self.clave:
            return(self.clave)
        else:
            return(self.nombre)


class Companhia(models.Model):
    id = models.AutoField(primary_key=True)
    razon_social = models.TextField(db_column='razonSocial', blank=True, null=True)  # Field name made lowercase.
    nombre = models.TextField(blank=True, null=True)
    rfc = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'companhia'

    def __str__(self):
        return(self.nombre)


class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.TextField(blank=True, null=True)
    apellidos = models.TextField(blank=True, null=True)
    razon_social = models.TextField(db_column='razonSocial', blank=True, null=True)
    rfc = models.TextField(blank=True, null=True)
    clave = models.CharField(max_length=4, blank=True, null=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, models.SET_NULL, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'persona'

    def __str__(self):
        if self.usuario:
            return str(self.usuario)
        elif self.clave:
            return(self.clave)
        else:
            return("{0} {1}".format(self.nombres, self.apellidos))

class Direccion(models.Model):
    id = models.AutoField(primary_key=True)
    cp = models.TextField(blank=True, null=True)
    calle = models.TextField(blank=True, null=True)
    numero = models.TextField(blank=True, null=True)
    colonia = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    estado = models.ForeignKey('Estado', models.DO_NOTHING, db_column='fk_estado', blank=True, null=True)
    codigo_plus = models.TextField(db_column='codigoPlus', blank=True, null=True)  # Field name made lowercase.
    utm_x = models.FloatField(blank=True, null=True)
    utm_y = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'direccion'

    def __str__(self):
        return("{0} {1}".format(self.calle, self.numero))
