# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils.text import slugify
from datetime import datetime


class Areasproy(models.Model):
    pk_id = models.AutoField(primary_key=True)
    supconstsnb = models.FloatField(db_column='supConstSNB', blank=True, null=True)  # Field name made lowercase.
    supconstbnb = models.FloatField(db_column='supConstBNB', blank=True, null=True)  # Field name made lowercase.
    supdesplante = models.FloatField(db_column='supDesplante', blank=True, null=True)  # Field name made lowercase.
    suppavimentos = models.FloatField(db_column='supPavimentos', blank=True, null=True)  # Field name made lowercase.
    supverdeperm = models.FloatField(db_column='supVerdePerm', blank=True, null=True)  # Field name made lowercase.
    supverdeimper = models.FloatField(db_column='supVerdeImper', blank=True, null=True)  # Field name made lowercase.
    supotraslibres = models.FloatField(db_column='supOtrasLibres', blank=True, null=True)  # Field name made lowercase.
    version = models.TextField(blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)
    fk_proyecto = models.ForeignKey('Proyecto', models.CASCADE, db_column='fk_proyecto',
        blank=True, null=True)
    fk_obs = models.ForeignKey('Obs', models.CASCADE, db_column='fk_obs',
        blank=True, null=True)
    stampcrea = models.DateTimeField(db_column='stampCrea', blank=True, null=True)  # Field name made lowercase.
    stampmod = models.DateTimeField(db_column='stampMod', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'areasProy'


class Obs(models.Model):
    pk_id = models.AutoField(primary_key=True)
    obs = models.TextField(blank=True, null=True)
    stampcrea = models.DateTimeField(default=datetime.now, db_column='stampCrea', blank=True, null=True)  # Field name made lowercase.
    stampmod = models.DateTimeField(auto_now_add=True, db_column='stampMod', blank=True, null=True)  # Field name made lowercase.
    fk_creador = models.IntegerField(blank=True, null=True)
    fk_modif = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'obs'


class TipoProyecto(models.Model):
    pk_id = models.AutoField(primary_key=True)
    clave = models.TextField(max_length=35, null=False, blank=False)
    nombre = models.TextField(null=False, blank=False)
    plazoentrega  = models.IntegerField('Plazo_días_hábiles', null=True, blank=True)

    def __str__(self):
        return(self.clave)

class Proyecto(models.Model):
    pk_id = models.AutoField(primary_key=True)
    slug = models.SlugField(editable=False)
    nombre = models.TextField(blank=True, null=True)
    clave = models.TextField(default='', max_length=35)
    fk_tipo = models.ForeignKey('TipoProyecto', models.DO_NOTHING, blank=True,
        null=True)
    cliente = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    fechainicio = models.DateField(db_column='fechaInicio', blank=True, null=True)  # Field name made lowercase.
    fechafin = models.DateField(db_column='fechaFin', blank=True, null=True)  # Field name made lowercase.
    estado = models.TextField(blank=True, null=True)
    avance = models.FloatField(blank=True, null=True)
    fk_proyectopadre = models.ForeignKey('self', models.CASCADE, blank=True, null=True)  # Field name made lowercase.
    fk_predio = models.IntegerField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    stampcrea = models.DateTimeField(default=datetime.now, db_column='stampCrea',
        blank=True, null=True, editable=False)  # Field name made lowercase.
    stampmod = models.DateTimeField(auto_now_add=True, db_column='stampMod', blank=True, null=True)  # Field name made lowercase.
    miembros = models.ManyToManyField('directorio.Persona', through='Brigada')

    def __str__(self):
        return("{0} {1}".format(self.tipo, self.clave))

    def save(self, *args, **kwargs):
        if not self.pk_id:
            self.slug = slugify("{0}-{1}".format(self.tipo, self.clave))
        super(Proyecto,self).save(*args, **kwargs)


    class Meta:
        managed = True
        db_table = 'proyecto'


class Brigada(models.Model):
    proyecto = models.ForeignKey('Proyecto', models.CASCADE)
    miembro = models.ForeignKey('directorio.Persona', models.CASCADE)
    companhia = models.ForeignKey('directorio.Companhia', models.CASCADE)
    funcion = models.CharField(max_length=140, blank=True, null=True)
    activo = models.BooleanField(default=True)
