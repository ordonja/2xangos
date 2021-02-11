# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.db.models import signals


from dosxangos.certificaciones.models import Certificacion as ProyectoCert

#crea proyecto certificacion si proyecto creado es PCES
def crea_proyecto_cert(sender,instance,created,**kwargs):
    if created and instance.fk_tipo.clave == "PCES 2020" or instance.fk_tipo.clave=="PCES 2008":
            proyecto_cert = ProyectoCert.objects.create(proyecto=instance, slug=instance.slug)


class Obs(models.Model):
    id = models.AutoField(primary_key=True)
    obs = models.TextField(blank=True, null=True)
    stamp_crea = models.DateTimeField(default=timezone.now, db_column='stampCrea', blank=True, null=True)  # Field name made lowercase.
    stamp_mod = models.DateTimeField(auto_now_add=True, db_column='stampMod', blank=True, null=True)  # Field name made lowercase.
    fk_creador = models.IntegerField(blank=True, null=True)
    fk_modif = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'obs'


class TipoProyecto(models.Model):
    id = models.AutoField(primary_key=True)
    clave = models.TextField(max_length=35, null=False, blank=False)
    nombre = models.TextField(null=False, blank=False)
    plazo_entrega  = models.IntegerField('Plazo_días_hábiles', null=True, blank=True)
    fk_tipo_padre  = models.ForeignKey('self', on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        if self.fk_tipo_padre:
            return("{0} {1}".format(self.fk_tipo_padre.clave, self.clave))
        return(self.clave)

class Proyecto(models.Model):
    class EtapaChoices(models.TextChoices):
        dc = '1', "DISEÑO Y CONSTRUCCION"
        op = '2', "OPERACIÓN"

    id = models.AutoField(primary_key=True)
    slug = models.SlugField(editable=False)
    nombre = models.TextField(blank=True, null=True)
    clave = models.TextField(default='', max_length=35)

    cliente = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateField(db_column='fechaInicio', blank=True, null=True)  # Field name made lowercase.
    fecha_fin = models.DateField(db_column='fechaFin', blank=True, null=True)  # Field name made lowercase.
    etapa = models.TextField(blank=True, null=True, choices=EtapaChoices.choices)
    avance = models.FloatField(blank=True, null=True)
    fk_proyecto_padre = models.ForeignKey('self', models.CASCADE, blank=True, null=True)  # Field name made lowercase.
    activo = models.BooleanField(default=True, blank=True, null=True)

    predios = models.ManyToManyField('espacios.Predio', blank=True)
    fk_tipo = models.ForeignKey(TipoProyecto, models.DO_NOTHING, blank=True,
        null=True)
    fk_obs = models.ManyToManyField(Obs, blank=True)
    miembros = models.ManyToManyField('directorio.Persona', through='Brigada')

    class Meta:
        managed = True
        db_table = 'proyectos'

    def __str__(self):
        return(self.slug)

    def lista_campos(self):
        return [(field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields]

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify("{0}-{1}".format(self.fk_tipo.clave, self.clave))
            super(Proyecto,self).save(*args, **kwargs)
            Brigada.objects.create(proyecto=self)
        super(Proyecto,self).save(*args, **kwargs)

signals.post_save.connect(crea_proyecto_cert, sender=Proyecto,
    dispatch_uid='models.crea_proyecto_cert')



class Brigada(models.Model):
    proyecto = models.ForeignKey(Proyecto, models.CASCADE)
    miembro = models.ForeignKey('directorio.Persona', on_delete=models.CASCADE, default=1)
    companhia = models.ForeignKey('directorio.Companhia', models.CASCADE, default=1)
    funcion = models.CharField(max_length=140, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return("{0} {1}".format(self.proyecto, self.miembro))
