from django.db import models

# Create your models here.
class User(models.Model):
    """Define la tabla User"""
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=60, null=True, blank=True)
    email = models.EmailField()
    fechaNacimiento = models.DateField(null=True, blank=True)
    GENERO = [
        ("H","Hombre"),
        ("M","Mujer"),
    ]
    genero = models.CharField(max_length=1, choices = GENERO)
    clave = models.CharField(max_length=40, null=True, blank=True)
    tipo = models.CharField(max_length=44, null=True, blank=True)

    def __str__(self):
        """Se define la representacion en str para User"""
        return "{} {}".format(self.nombre, self.apellidos)

class Zona(models.Model):
    """Define la tabla Zona"""
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=256, null=True, blank=True)
    latitud = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)
    longitud = models.DecimalField(max_digits=8,decimal_places=6, null=True, blank=True)

    def __str__(self):
        """Se define la representacion en str para Zona"""
        return "{} {}".format(self.nombre, self.descripcion)

class Tour(models.Model):
    """Define la tabla Tour"""
    nombre = models.CharField(max_length=145)
    slug = models.CharField(max_length=45, null=True, blank=True)
    operador = models.CharField(max_length=45, null=True, blank=True)
    tipoDeTour = models.CharField(max_length=45, null=True, blank=True)
    descripcion = models.CharField(max_length=256)
    img = models.CharField(max_length=45, null=True, blank=True)
    pais = models.CharField(max_length=45, null=True, blank=True)
    zonaSalida = models.ForeignKey(Zona, on_delete=models.SET_NULL, null=True,
                 blank=True, related_name="tours_salida")
    zonaLlegada = models.ForeignKey(Zona, on_delete=models.SET_NULL, null=True,
                 blank=True, related_name="tours_llegada")
    
    def __str__(self):
        return "{}".format(self.nombre)

class Salida(models.Model):
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    asientos = models.PositiveSmallIntegerField(null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tour = models.ForeignKey(Tour, related_name="salidas", on_delete = models.CASCADE)

    def __str__(self):
        return "{} {} {}".format(self.tour, self.fechaInicio, self.fechaFin)

class Boleto(models.Model):
    metodo_pago = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="usuarios")
    salida_id = models.ForeignKey(Salida, on_delete=models.SET_NULL, null=True, blank=True, related_name="salidas")
    numero_asiento =models.CharField(max_length=4)
    puerta_salida = models.PositiveSmallIntegerField(null=True, blank=True)
    STATUS = [
        ("pending","pending"),
        ("approved","approved")
    ]
    status =models.CharField(max_length=15, choices=STATUS)

    def __str__(self):
        return "{} ({}, {}(".format(self.user_id, self.metodo_pago, self.fecha_fin)


