from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save


class Base(models.Model):
    stamp_crea = models.DateTimeField(default=timezone.now, blank=True, null=True, editable=False)  # Field name made lowercase.
    stamp_mod = models.DateTimeField(auto_now_add=True, blank=True, null=True) # Field name made lowercase.
    fk_obs = models.ManyToManyField('proyectos.Obs', blank=True)

    class Meta:
        abstract = True


class Meta(models.Model):
    id = models.AutoField(primary_key=True)
    meta = models.TextField(blank=True, null=True)
    aplica_dc = models.BooleanField(blank=True, null=True)
    aplica_op = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return(self.meta)


class Rubro(models.Model):
    id = models.AutoField(primary_key=True)
    version = models.IntegerField()
    rubro = models.CharField(max_length=70)
    clave = models.CharField(max_length=3)

    class Meta:
        db_table = 'cert_rubro'

    def __str__(self):
        return(self.clave)


class EvidenciaReq(models.Model):
    id = models.AutoField(primary_key=True)
    evidencia_req = models.TextField()
    fk_evid_padre = models.ForeignKey('self',on_delete=models.CASCADE, blank=True,
        null=True)

    def __str__(self):
        return(self.evidencia_req)


class EvidenciaCriterio(Base):
    id = models.AutoField(primary_key=True)
    fk_evidencia_req = models.ForeignKey('EvidenciaReq',on_delete=models.CASCADE)
    fk_criterio = models.ForeignKey('Criterio',on_delete=models.CASCADE)
    aplica_dc = models.BooleanField(blank=True, null=True)
    aplica_op = models.BooleanField(blank=True, null=True)

    class Meta:
        ordering = ['fk_criterio', 'fk_evidencia_req']

    def __str__(self):
        return("{0} {1}".format(self.fk_criterio.id, self.fk_evidencia_req.id))


class Indicador(models.Model):
    id = models.AutoField(primary_key=True)
    clave = models.CharField(max_length=20,blank=True, null=True)
    clave_sedema = models.CharField(max_length=20,blank=True, null=True)
    definicion =  models.TextField(blank=True, null=True)
    unidad = models.CharField(max_length=20,blank=True, null=True)

    def __str__(self):
        return(self.clave)


class Requerimiento(models.Model):
    id = models.AutoField(primary_key=True)
    req = models.TextField(blank=True, null=True)

    req_padre = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='reqpadre')

    def __str__(self):
        return(self.req)


class Criterio(Base):
    id = models.AutoField(primary_key=True)
    clave=models.CharField(max_length=5, blank=True, null=True)
    nombre = models.CharField(max_length=140, blank=True, null=True)
    objetivo = models.TextField(blank=True, null=True)
    aplica_dc = models.BooleanField(blank=True, null=True)
    aplica_op = models.BooleanField(blank=True, null=True)
    obligatorio_dc = models.BooleanField(blank=True, null=True)
    puntos_dc = models.IntegerField(blank=True, null=True)
    obligatorio_op = models.BooleanField(blank=True, null=True)
    puntos_op = models.IntegerField(blank=True, null=True)

    metas = models.ManyToManyField('Meta', blank=True)
    indicadores = models.ManyToManyField('Indicador', blank=True,
        related_name="criterio_ind")
    requerimientos = models.ManyToManyField('Requerimiento', blank=True,
        related_name="criterio_req")
    aplica_tipo_proyecto=models.ManyToManyField('proyectos.Tipoproyecto', blank=True)
    fk_rubro = models.ForeignKey('Rubro', on_delete=models.CASCADE, db_column='fk_rubro', blank=True, null=True)
    evidencias = models.ManyToManyField('EvidenciaReq', through='EvidenciaCriterio')

    class Meta:
        db_table = 'cert_criterio'
        ordering = ['id', 'clave']

    def __str__(self):
        return("{0} {1}".format(self.clave, self.nombre))


class Certificacion(models.Model):
    proyecto = models.OneToOneField('proyectos.Proyecto',on_delete=models.CASCADE,primary_key=True,
        limit_choices_to={'fk_tipo': 3, 'fk_tipo':4}, related_name='proyecto_cert')
    slug = models.SlugField(editable=True)
    criterios = models.ManyToManyField('Criterio', through='CriterioProyecto')

    def __str__(self):
        return(self.proyecto.clave)


class CriterioProyecto(Base):
    id = models.AutoField(primary_key=True)
    cumple = models.BooleanField(blank = True, null = True)
    puntos_obtenidos = models.IntegerField(blank=True, null=True)

    fk_proyecto = models.ForeignKey(Certificacion,on_delete=models.CASCADE)
    fk_criterio = models.ForeignKey(Criterio,on_delete=models.CASCADE)

    indicadores = models.ManyToManyField('Indicador', through='IndicadorProyecto',
        blank=True, related_name="cert_ind")
    requerimientos = models.ManyToManyField('Requerimiento',
        through='RequerimientoProyecto', blank=True, related_name="cert_req")
    evidencias = models.ManyToManyField('EvidenciaCriterio', through='EvidenciaProyecto',
        related_name="cert_evid")

    class Meta:
            ordering=['fk_proyecto', 'fk_criterio']

    def __str__(self):
        return("{0}.{1}".format(self.fk_proyecto, self.fk_criterio))

    def lista_campos(self):
        return [(field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields]

    @receiver(post_save, sender=Certificacion)
    def crea_lista_criterios(sender, created, instance, **kwargs):
        if created:
            if instance.proyecto.etapa == '1':
                criterios_todos = Criterio.objects.filter(aplica_dc=True)
            elif instance.proyecto.etapa == '2':
                criterios_todos = Criterio.objects.filter(aplica_op=True)

            for criterio in criterios_todos:
                CriterioProyecto.objects.create(fk_proyecto = instance, fk_criterio = criterio)


class IndicadorProyecto(Base):
    id = models.AutoField(primary_key=True)
    fk_criterio_proyecto = models.ForeignKey('CriterioProyecto',on_delete=models.CASCADE)
    fk_indicador = models.ForeignKey('Indicador',on_delete=models.CASCADE, blank=True, null=True)
    valor_indicador = models.FloatField(blank=True,null=True)
    cumple = models.BooleanField(blank=True, null=True)

    def __str__(self):
        if self.cumple:
            return("{0}.{1}.{2}".format(self.cumple, self.fk_criterio_proyecto, self.fk_indicador))
        else:
            return(" .{0}.{1}".format(self.fk_criterio_proyecto, self.fk_indicador))

    @receiver(post_save, sender=CriterioProyecto)
    def crea_lista_indicadores(sender, created, instance, **kwargs):
        if created:
            indicadores = instance.fk_criterio.indicadores.exclude(clave='NoAp')
            for indicador in indicadores:
                IndicadorProyecto.objects.create(fk_criterio_proyecto=instance,
                    fk_indicador=indicador)


class RequerimientoProyecto(Base):
    id = models.AutoField(primary_key=True)
    fk_criterio_proyecto = models.ForeignKey(CriterioProyecto,on_delete=models.CASCADE)
    fk_req = models.ForeignKey(Requerimiento, on_delete=models.CASCADE, blank=True, null=True)
    cumple = models.BooleanField(blank=True, null=True)

    @receiver(post_save, sender=CriterioProyecto)
    def crea_lista_requerimientos(sender, created, instance, **kwargs):
        if created:
            requerimientos = instance.fk_criterio.requerimientos.all()
            for requerimiento in requerimientos:
                RequerimientoProyecto.objects.create(fk_criterio_proyecto=instance,
                    fk_req=requerimiento)


class EvidenciaProyecto(Base):
    id = models.AutoField(primary_key=True)
    fk_evidencia = models.ForeignKey(EvidenciaCriterio,on_delete=models.CASCADE)
    fk_criterio = models.ForeignKey('CriterioProyecto',on_delete=models.CASCADE)
    cumple = models.BooleanField(blank=True, null=True)
    evidencia_presentada = models.CharField(max_length=140, null=True, blank=True)

    def __str__(self):
        if self.cumple:
            return("{0}.{1}.{2}".format(self.cumple, self.fk_criterio, self.fk_evidencia))
        else:
            return(" .{0}.{1}".format(self.fk_criterio, self.fk_evidencia))

    @receiver(post_save, sender=CriterioProyecto)
    def crea_lista_evidencias(sender, created, instance, **kwargs):
        if created:
            if instance.fk_proyecto.proyecto.etapa == '1':
                evidencias = EvidenciaCriterio.objects.filter(fk_criterio = instance.fk_criterio, aplica_dc=True)
            if instance.fk_proyecto.proyecto.etapa == '2':
                evidencias = EvidenciaCriterio.objects.filter(fk_criterio = instance.fk_criterio, aplica_op=True)
            for evidencia in evidencias:
                EvidenciaProyecto.objects.create(fk_evidencia=evidencia,
                    fk_criterio=instance)
