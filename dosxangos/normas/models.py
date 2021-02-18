from django.db import models
from django.utils import timezone


class Base(models.Model):
    stamp_crea = models.DateTimeField(default=timezone.now, blank=True, null=True, editable=False)  # Field name made lowercase.
    stamp_mod = models.DateTimeField(auto_now_add=True, blank=True, null=True) # Field name made lowercase.
    fk_obs = models.ManyToManyField('proyectos.Obs', blank=True)
    class Meta:
        abstract = True


# ENER, AMBT, SEMARNAT
class EmisorAmbito(models.Model):
    id = models.AutoField(primary_key=True)
    clave = models.CharField(max_length=20,blank=True, null=True)
    nombre = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return(self.clave)

# Libro, sección, artículo, inciso, párrafo, etc.
class Seccion(models.Model):
    class TipoChoices(models.TextChoices):
        libro = '1', "Libro"
        titulo = '2', "Título"
        capitulo = '3', "Capítulo"
        seccion = '4', "Sección"
        articulo = '5', "Art."
        parrafo = '6', "P."
        apartado = '7', "Apartado"
        fraccion = '8', "fr."
        inciso  = '9', "inciso"

    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=60, blank=True, null=True, choices=TipoChoices.choices)
    numero = models.CharField(max_length = 40, blank=True, null=True)
    texto =  models.TextField(blank=True, null=True)
    seccion_padre = models.ForeignKey('self',on_delete=models.CASCADE, blank=True,
        null=True)

    def __str__(self):
        return("{0} {1}".format(self.tipo, self.numero))


class Norma(Base):
    class Competencia(models.TextChoices):
        estatal = '1', "estatal"
        municipal = '2', "municipal"
        federal = '3', "federal"
        internacional = '4', "internacional"

    class Tipo(models.TextChoices):
        nom = '1', "NOM"
        nadf = '2', "NADF"
        nmx = '3', "NMX"
        ntc = '4', "NTC"
        ntea = '5', "NTEA"
        proynom = '6', "PROY-NOM"
        ley = '10', "Ley"
        reg = '20', "Reglamento"
        otro = '100', "Otro"

    id = models.AutoField(primary_key=True)
    competencia = models.CharField(max_length=10, blank=True,
        choices=Competencia.choices)
    tipo = models.CharField(max_length=10, blank=True, null=True,
        choices=Tipo.choices)
    rubro = models.CharField(max_length=10, blank=True, null=True)
    numero = models.CharField(max_length=10, blank=True, null=True)
    emisor_ambito = models.ForeignKey('EmisorAmbito', on_delete=models.SET_NULL,
        blank=True, null=True)
    anho = models.CharField(max_length=10, blank=True, null=True)

    clave = models.CharField(max_length=140, blank=True, null=True)
    nombre = models.CharField(max_length=280, blank=True, null=True)
    descripcion  = models.TextField(blank=True, null=True)
    secciones = models.ManyToManyField('Seccion', blank=True)

    def save(self, *args, **kwargs):
        if not self.id and self.tipo < 10:
            if not self.rubro:
                self.clave = ("{0}-{1}-{3}-{4}".format(self.tipo, self.numero,
                    self.emisor_ambito, self.anho))
            else:
                self.clave = ("{0}-{1}-{3}-{4}-{5}".format(self.tipo, self.rubro,self.numero,
                    self.emisor_ambito, self.anho))
        super(Norma, self).save(*args, **kwargs)


    def __str__(self):
        return(self.clave)


# Create your models here.
