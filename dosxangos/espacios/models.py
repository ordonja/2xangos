from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone


class Base(models.Model):
    stamp_crea = models.DateTimeField(default=timezone.now, blank=True, null=True, editable=False)  # Field name made lowercase.
    stamp_mod = models.DateTimeField(auto_now_add=True, blank=True, null=True) # Field name made lowercase.
    fk_obs = models.ManyToManyField('proyectos.Obs', blank=True)
    class Meta:
        abstract=True

class Superficie(models.Model):
    class TipoChoices(models.TextChoices):
        total = '1', "total"
        const = '2', "construida"
        despĺante = '3', "desplante"
        libre = '4', "libre"
        verde = '5', "verde"
        pavimentada = '6', "pavimentada"
        permeable = '7', "permeable"
        bnb = '8', "BNB"
        snb = '9', "SNB"
        cajones_est = '10', "cajones_est"
        restriccion = '40', "restricción"
        max_desplante = '20', "max_desplante"
        max_const= '21', "max_const"
        libre_req= '22', "libre_req"
        cajones_est_req = '30', "cajones_est_req"
        otra = '50', "otra"
    pk_id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=4,default=1,blank=True, null=True, choices=TipoChoices.choices)
    area = models.FloatField('m²',default=0.0, blank=True, null=True)
    espacio = models.ForeignKey('Espacio', models.CASCADE)

    def __str__(self):
        return("{0} {1}".format(self.espacio, self.tipo))


class Espacio(Base):
    pk_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=120, blank=True, null=True)

    fk_espaciopadre = models.ForeignKey('self', models.CASCADE,
        db_column='fk_espacioPadre', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'espacios'

    def __str__(self):
        return self.nombre

    @receiver(post_save, sender='espacios.Edificio')
    def crea_pisos(sender, created, instance, **kwargs):
        if created:
            for nivel in range(0, instance.niveles_snb):
                nombre_nivel = nivel
                Espacio.objects.create(nombre=nombre_nivel,fk_espaciopadre_pk_id=instance.pk_id)
            if instance.niveles_snb >0:
                for nivel in range(1, instance.niveles_bnb + 1):
                    nombre_nivel = "-{0}".format(nivel)
                    Espacio.objects.create(nombre=nombre_nivel,fk_espaciopadre_pk_id=instance.pk_id)

class Predio(Espacio):
    proyecto = models.ManyToManyField('proyectos.Proyecto', blank=True)
    cuenta_predial = models.CharField(max_length=120, blank=True, null=True)
    direccion = models.ForeignKey('directorio.Direccion',on_delete=models.SET_NULL, blank=True, null=True)
    zonificaciones = models.ManyToManyField('Zonificacion', blank=True)

    def __str__(self):
        return self.direccion


class Zonificacion(Espacio):
    clave = models.CharField(max_length=120, blank=True, null=True)
    ordenamiento = models.CharField(max_length=120, blank=True, null=True)
    fecha =models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.clave


class Edificio(Espacio):
    proyecto = models.ManyToManyField('proyectos.Proyecto', blank=True)
    uso_principal = models.CharField(max_length=70, blank=True, null=True)
    niveles_snb = models.IntegerField(default=1,blank=True, null=True)
    niveles_bnb = models.IntegerField(blank=True, null=True)
