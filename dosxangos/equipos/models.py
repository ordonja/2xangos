from django.db import models
from django.utils import timezone
from model_utils.managers import InheritanceManager

class classproperty(property):
    def __get__(self, cls, owner):
        return self.fget.__get__(None,owner)()


class Base(models.Model):
    stamp_crea = models.DateTimeField(default=timezone.now, blank=True, null=True, editable=False)  # Field name made lowercase.
    stamp_mod = models.DateTimeField(auto_now_add=True, blank=True, null=True) # Field name made lowercase.
    fk_obs = models.ManyToManyField('proyectos.Obs', blank=True)

    class Meta:
        abstract = True


class Equipo(Base):
    class EnerChoices(models.TextChoices):
        el = '0', "electricidad"
        ds = '1', "diesel"
        gnat = '2', "gas natural"
        glp = '3', "gas LP"
        gasol = '4', "gasolina"

    id = models.AutoField(primary_key=True)
    equipo_tipo = models.ForeignKey('Tipoequipo', models.DO_NOTHING, db_column='fk_equipoTipo', blank=True, null=True)  # Field name made lowercase.
    marca = models.TextField(blank=True, null=True)
    modelo = models.TextField(blank=True, null=True)
    potencia = models.FloatField(blank=True, null=True)
    unidad_potencia = models.ForeignKey('UnidadMedicion', on_delete= models.SET_NULL,
        db_column='fk_unidadPotencia', blank=True, null=True, related_name="eq_potencia")  # Field name made lowercase.
    eficiencia = models.FloatField('%\u03B7', blank=True, null=True)
    fuente_ener = models.TextField(db_column='fuenteEner', blank=True, null=True, choices=EnerChoices.choices)  # Field name made lowercase.
    equipo_padre = models.ForeignKey('self', on_delete= models.SET_NULL,
    db_column='fk_equipoPadre', blank=True, null=True,
    related_name='equipo_hijo')  # Field name made lowercase.
    normas = models.ManyToManyField('normas.Norma', through='NormaEquipo',
    blank=True, related_name="equipo_norma")
    pais_origen = models.ForeignKey('directorio.Pais', on_delete= models.SET_NULL, verbose_name="pais",
        related_name="equipos", db_column='fk_paisOrigen', blank=True, null=True)  # Field name made lowercase.
    ficha_tec = models.TextField( blank=True, null=True)  # Field name made lowercase.
    url_ft = models.TextField(blank=True, null=True)  # This field type is a guess.
    anho_fabricacion = models.IntegerField('año fabricación',db_column='anhoFabricacion', blank=True, null=True)  # Field name made lowercase.

    objects = InheritanceManager()

    class Meta:
        verbose_name = 'equipo general'
        verbose_name_plural = 'equipos generales'


    def __str__(self):
        return("{0} {1} {2}".format(
        self.equipo_tipo, self.marca, self.modelo))

    @classproperty
    @classmethod
    def SUBCLASS_OBJECT_CHOICES(cls):
        "All known subclasses, keyed by a unique name per class subclass choices, with nice names"

        return {rel.name: rel.related_model
            for rel in cls._meta.related_objects
            if rel.parent_link
        }

    @classproperty
    @classmethod
    def CLASS_CHOICE(cls):
        return [
        (cls._meta.model_name, cls._meta.verbose_name)
        ]


    @classproperty
    @classmethod
    def SUBCLASS_CHOICES(cls):
        "Available subclass choices, with nice names"
        return [
            (name, model._meta.verbose_name)
            for name, model in cls.SUBCLASS_OBJECT_CHOICES.items()
        ]

    @classmethod
    def SUBCLASS(cls, name):
        "Given a subclass name, return the subclass."
        return cls.SUBCLASS_OBJECT_CHOICES.get(name, cls)


class NormaEquipo(Base):
    class CumpleChoices(models.TextChoices):
        no = '0', "No"
        si = '1', "Sí"
        posible = '2', "Posible"
        imposible = '3', "Imposible"
        desconocido = '4', "Desconocido"

    id = models.AutoField(primary_key=True)
    fk_equipo = models.ForeignKey('Equipo', on_delete=models.CASCADE)
    fk_norma = models.ForeignKey('normas.Norma',on_delete=models.CASCADE, blank=True, null=True)
    requerimiento = models.FloatField(blank=True,null=True)
    descripcion_requerimimiento = models.CharField(max_length=70, blank=True, null=True)
    cumple =  models.TextField(blank=True, null=True, choices=CumpleChoices.choices)

    def __str__(self):
        return(self.fk_norma.clave)

class EquipoProyecto(Base):
    id = models.AutoField(primary_key=True)
    serial = models.TextField(blank=True, null=True)
    cantidad = models.FloatField(blank=True,null=True)

    equipo = models.ForeignKey('Equipo', on_delete=models.CASCADE)
    proyecto = models.ForeignKey('proyectos.Proyecto',
    on_delete=models.CASCADE, related_name='equipo_proy')
    espacios = models.ManyToManyField('espacios.Espacio',
    blank=True, related_name="equipo_esp")
    foto = models.CharField(max_length=140, blank=True, null=True)

    def __str__(self):
        return("{0}.{1} {2} {3}".format(
        self.proyecto, self.equipo.equipo_tipo, self.equipo.marca, self.equipo.modelo))

class TipoEquipo(models.Model):
    tipo = models.TextField(blank=True, null=True)
    clave = models.CharField(max_length=20, blank=True, null=True)
    fk_norma = models.IntegerField(blank=True, null=True)
    fk_supertipo = models.ForeignKey('self', on_delete= models.SET_NULL, db_column='fk_supertipo', blank=True, null=True)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return(self.clave)

class UnidadMedicion(models.Model):
    class SistemaChoices(models.TextChoices):
        SI = '0', "SI"
        BU = '1', "BU"

    id = models.AutoField(primary_key=True)
    sistema = models.TextField(blank=True, null=True, choices=SistemaChoices.choices)
    unidad = models.TextField(blank=True, null=True)
    simbolo = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "unidad"
        verbose_name_plural = "unidades"

    def __str__(self):
        return(self.simbolo)


class MotorElectrico(Equipo):
    class FrameType(models.TextChoices):
        abierto = '0', "abierto"
        cerrado = '1', "cerrado"
    equipo = models.OneToOneField('Equipo', parent_link=True, on_delete=models.CASCADE)
    rpm = models.FloatField(null=True, blank=True)
    frame = models.CharField(max_length=20, blank=True, null=True)
    frame_type = models.TextField(blank=True, null=True, choices=FrameType.choices)
    poles = models.FloatField(null=True, blank=True)
    voltaje = models.FloatField('V',null=True, blank=True)
    amperaje = models.FloatField('A', null=True, blank=True)
    frecuencia = models.FloatField('Hz', null=True, blank=True)
    nema_premium = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'motor eléctrico'
        verbose_name_plural = 'motores eléctricos'

    def __str__(self):
        return("{0} {1} {2}".format(
        self.equipo.equipo_tipo, self.equipo.marca, self.equipo.modelo))
