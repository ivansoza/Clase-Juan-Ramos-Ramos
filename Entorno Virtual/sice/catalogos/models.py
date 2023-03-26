from django.db import models

# Create your models here.

# Crea una clase llamada Vehiculo que hereda de la clase Model.

#La tabla base que hereda la llava va antes donde la va a ocupar
class Vehiculo(models.Model):
# Creando una tabla llamada Vehiculo con dos columnas: NIV y noMotor.
    NIV = models.CharField(max_length=20, help_text="NIV del vehiculo")
    noMotor =models.CharField(max_length=30,blank=True)
    marca = models.CharField(max_length=40)
    linea =  models.CharField(max_length=40)
    modelo = models.CharField(max_length=4)

    def __str__(self):
        return '%s - %s - %s' % (self.NIV,self.marca,self.linea)
    
    
    def __save__(self):
        self.NIV = self.NIV.upper()
        self.noMotor = self.noMotor.upper()
        super(Vehiculo,self).save()

    class Meta:
        verbose_name_plural = "VEHICULOS"
        db_table = 'vehiculo'


class Propietario(models.Model):
    RFC = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apPaterno = models.CharField(max_length=30)
    apMaterno = models.CharField(max_length=30)
    email = models.EmailField( max_length=40)
    CURP = models.CharField(max_length=50)
    calle = models.CharField(max_length=50)
    colonia = models.CharField(max_length=40)
    municipio = models.CharField(max_length=40)
    CP = models.CharField(max_length=5)
    edad = models.IntegerField(default=0)
    
    def __str__(self):
        return "%s %s %s" % (self.nombre, self.apPaterno, self.apMaterno)
    
    def save(self, *args, **kwargs):
        self.CURP = self.CURP.upper()
        super().save(*args, **kwargs)



class Oficina(models.Model):
    nombre = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=40)
    telefono = models.CharField(max_length=10)

    def __str__(self):
        return ("%s" % self.nombre)

class Placa(models.Model):
    numero = models.CharField(max_length=10)
    numTC = models.CharField(max_length=20)
    fecha = models.DateField(auto_now=True)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    propietario= models.ForeignKey(Propietario, on_delete=models.CASCADE)
    estatus = models.BooleanField(default=True)
    oficina = models.ForeignKey(Oficina, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s"% self.numero, self.vehiculo
    
    