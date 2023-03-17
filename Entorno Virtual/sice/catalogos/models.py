from django.db import models

# Create your models here.

# Crea una clase llamada Vehiculo que hereda de la clase Model.

#La tabla base que hereda la llava va antes donde la va a ocupar
class Vehiculo(models.Model):
# Creando una tabla llamada Vehiculo con dos columnas: NIV y noMotor.
    NIV = models.CharField(max_length=20, help_text="NIV del vehiculo")
    noMotor =models.CharField(max_length=30,blanck=True)
    marca = models.CharField(_max_length=40)
    linea =  models.CharField(max_length=40)
    modelo = models.CharField(_max_length=4)
class Propietario(models.Model):
    pass

class Oficina(models.Model):
    pass

class Placa(models.Model):
    pass