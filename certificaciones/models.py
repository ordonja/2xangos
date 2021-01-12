from django.db import models

class Criterio(models.Model):
    pk_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=140, blank=True, null=True)
    objetivo = models.TextField(blank=True, null=True)
    aplica_dc = models.BooleanField(blank=True, null=True)
    aplica_op = models.BooleanField(blank=True, null=True)
    obligatorio_dc = models.BooleanField(blank=True, null=True)
    puntos_dc = models.IntegerField(blank=True, null=True)
    obligatorio_op = models.BooleanField(blank=True, null=True)
    puntos_op = models.IntegerField(blank=True, null=True)
    fk_rubro = models.ForeignKey('Rubro', models.DO_NOTHING, db_column='fk_rubro', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cert_criterio'


class CertEvidReq(models.Model):
    pk_id = models.AutoField(primary_key=True)
    clave = models.CharField(max_length=10, blank=True, null=True)
    requerimiento = models.TextField(blank=True, null=True)
    pk_criterio = models.ForeignKey(Criterio, models.DO_NOTHING, db_column='pk_criterio', blank=True, null=True)
    aplica_dc = models.BooleanField(blank=True, null=True)
    aplica_op = models.BooleanField(blank=True, null=True)
    fk_criterio_padre = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cert_evid_req'


class EvidenciaReq(models.Model):
    pk_id = models.AutoField(primary_key=True)
    evidencia_req = models.TextField()

    class Meta:
        managed = False
        db_table = 'cert_evidencia_req'


class Rubro(models.Model):
    pk_id = models.AutoField(primary_key=True)
    version = models.IntegerField()
    rubro = models.CharField(max_length=70)
    clave = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'cert_rubro'
