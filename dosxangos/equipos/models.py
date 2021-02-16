from django.db import models
from django.utils import timezone


class Base(models.Model):
    stamp_crea = models.DateTimeField(default=timezone.now, blank=True, null=True, editable=False)  # Field name made lowercase.
    stamp_mod = models.DateTimeField(auto_now_add=True, blank=True, null=True) # Field name made lowercase.
    fk_obs = models.ManyToManyField('proyectos.Obs', blank=True)

    class Meta:
        abstract = True


class Equipo(Base):
    id = models.AutoField(primary_key=True)
    equipo_tipo = models.ForeignKey('Tipoequipo', models.DO_NOTHING, db_column='fk_equipoTipo', blank=True, null=True)  # Field name made lowercase.
    marca = models.TextField(blank=True, null=True)
    modelo = models.TextField(blank=True, null=True)
    serial = models.TextField(blank=True, null=True)
    pais_origen = models.ForeignKey('directorio.Pais', on_delete= models.SET_NULL, verbose_name="pais",
        related_name="equipos", db_column='fk_paisOrigen', blank=True, null=True)  # Field name made lowercase.
    ficha_tec = models.TextField( blank=True, null=True)  # Field name made lowercase.
    url_ft = models.TextField(blank=True, null=True)  # This field type is a guess.
    anho_fabricacion = models.IntegerField('año fabricación',db_column='anhoFabricacion', blank=True, null=True)  # Field name made lowercase.
    capacidad = models.FloatField(blank=True, null=True)
    fk_unidad_capacidad = models.ForeignKey('Unidadmedicion', on_delete= models.SET_NULL,
        db_column='fk_unidadCapacidad', blank=True, null=True, related_name="eq_capacidad")  # Field name made lowercase.
    potencia = models.FloatField(blank=True, null=True)
    fk_unidad_potencia = models.ForeignKey('Unidadmedicion', on_delete= models.SET_NULL,
        db_column='fk_unidadPotencia', blank=True, null=True, related_name="eq_potencia")  # Field name made lowercase.
    consumo_ener = models.FloatField(db_column='consumoEner', blank=True, null=True)  # Field name made lowercase.
    fk_unidad_ener = models.ForeignKey('Unidadmedicion', on_delete= models.SET_NULL,
        db_column='fk_unidadEner', blank=True, null=True, related_name="eq_energia")  # Field name made lowercase.
    fuente_ener = models.TextField(db_column='fuenteEner', blank=True, null=True)  # Field name made lowercase.
    fk_equipo_padre = models.ForeignKey('self', on_delete= models.SET_NULL, db_column='fk_equipoPadre', blank=True, null=True)  # Field name made lowercase.
    normas = models.ManyToManyField('normas.Norma', through='NormaEquipo',
    blank=True, related_name="equipo_norma")


class NormaEquipo(Base):
    class CumpleChoices(models.TextChoices):
        no = '0', "No"
        si = '1', "Sí"
        posible = '2', "Posible"
        imposible = '3', "Imposible"
        desconocido = '4', "Desconocido"

    id = models.AutoField(primary_key=True)
    fk_equipo = models.ForeignKey('Equipo', on_delete=models.CASCADE)
    fk_normal = models.ForeignKey('normas.Norma',on_delete=models.CASCADE, blank=True, null=True)
    requerimiento = models.FloatField(blank=True,null=True)
    descripcion_requerimimiento = models.CharField(max_length=70, blank=True, null=True)
    cumple =  models.TextField(blank=True, null=True, choices=CumpleChoices.choices)


class EquipoProyecto(Base):
    id = models.AutoField(primary_key=True)
    fk_equipo = models.ForeignKey('Equipo', on_delete=models.CASCADE)
    fk_proyecto = models.ForeignKey('proyectos.Proyecto',
    on_delete=models.CASCADE, related_name='equipo_proy')
    espacios = models.ManyToManyField('espacios.Espacio',
    blank=True, related_name="equipo_esp")


class TipoEquipo(models.Model):
    tipo = models.TextField(blank=True, null=True)
    fk_norma = models.IntegerField(blank=True, null=True)
    fk_supertipo = models.ForeignKey('self', on_delete= models.SET_NULL, db_column='fk_supertipo', blank=True, null=True)
    id = models.AutoField(primary_key=True)


class UnidadMedicion(models.Model):
    id = models.AutoField(primary_key=True)
    sistema = models.TextField(blank=True, null=True)
    unidad = models.TextField(blank=True, null=True)
    simbolo = models.TextField(blank=True, null=True)
