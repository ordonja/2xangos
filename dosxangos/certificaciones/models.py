from django.db import models
from datetime import datetime
from django.dispatch import receiver
from django.db.models.signals import post_save


class Base(models.Model):

    stamp_crea = models.DateTimeField(default=datetime.now, blank=True, null=True, editable=False)  # Field name made lowercase.
    stamp_mod = models.DateTimeField(auto_now_add=True, blank=True, null=True) # Field name made lowercase.

    class Meta:
        abstract = True


class Criterio(Base):
    pk_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=140, blank=True, null=True)
    objetivo = models.TextField(blank=True, null=True)
    aplica_dc = models.BooleanField(blank=True, null=True)
    aplica_op = models.BooleanField(blank=True, null=True)
    obligatorio_dc = models.BooleanField(blank=True, null=True)
    puntos_dc = models.IntegerField(blank=True, null=True)
    obligatorio_op = models.BooleanField(blank=True, null=True)
    puntos_op = models.IntegerField(blank=True, null=True)

    fk_obs = models.ForeignKey('proyectos.Obs', on_delete=models.CASCADE, db_column='fk_obs',
            blank=True, null=True)
    fk_rubro = models.ForeignKey('Rubro', on_delete=models.CASCADE, db_column='fk_rubro', blank=True, null=True)
    evidencias = models.ManyToManyField('EvidenciaReq', through='EvidenciaCriterio')

    class Meta:
        db_table = 'cert_criterio'

    def __str__(self):
        return(self.nombre)


class Rubro(models.Model):
    pk_id = models.AutoField(primary_key=True)
    version = models.IntegerField()
    rubro = models.CharField(max_length=70)
    clave = models.CharField(max_length=3)

    class Meta:
        db_table = 'cert_rubro'

    def __str__(self):
        return(self.clave)


class EvidenciaCriterio(Base):
    pk_id = models.AutoField(primary_key=True)
    fk_evidencia_req = models.ForeignKey('EvidenciaReq',on_delete=models.CASCADE)
    fk_criterio = models.ForeignKey(Criterio,on_delete=models.CASCADE)
    aplica_dc = models.BooleanField(blank=True, null=True)
    aplica_op = models.BooleanField(blank=True, null=True)

    class Meta:
        ordering = ['fk_criterio', 'fk_evidencia_req']

    def __str__(self):
        return("{0} {1}".format(self.fk_criterio.pk_id, self.fk_evidencia_req.pk_id))


class Proyecto(models.Model):
    pk_id = models.OneToOneField('proyectos.Proyecto',on_delete=models.CASCADE,primary_key=True,
        limit_choices_to={'pk_tipo': 3, 'pk_tipo':4}, related_name='proyecto_cert')
    criterios = models.ManyToManyField('Criterio', through='CriterioProyecto')

    def __str__(self):
        return(self.pk_id.clave)


class CriterioProyecto(Base):
    pk_id = models.AutoField(primary_key=True)
    fk_proyecto = models.ForeignKey('Proyecto',on_delete=models.CASCADE)
    fk_criterio = models.ForeignKey(Criterio,on_delete=models.CASCADE)
    cumple = models.BooleanField(blank = True, null = True)
    puntos_obtenidos = models.IntegerField(blank=True, null=True)
    evidencias = models.ManyToManyField('EvidenciaReq', through='EvidenciaCriterioProy')

#    @receiver(post_save, sender=Proyecto)
#   def crea_lista_criterios(sender, created, instance, **kwargs):
#    if created:



class EvidenciaReq(models.Model):
    pk_id = models.AutoField(primary_key=True)
    evidencia_req = models.TextField()
    fk_evid_padre = models.ForeignKey('self',on_delete=models.CASCADE,blank = True, null = True)
    def __str__(self):
        return(self.evidencia_req)


class EvidenciaCriterioProy(Base):
    pk_id = models.AutoField(primary_key=True)
    fk_evidencia_req = models.ForeignKey(EvidenciaReq,on_delete=models.CASCADE)
    fk_criterio = models.ForeignKey(CriterioProyecto,on_delete=models.CASCADE)
    cumple = models.BooleanField(blank = True, null = True)
