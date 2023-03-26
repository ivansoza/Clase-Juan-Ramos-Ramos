from django.db import models

# Create your models here.
options = [0, "Pedido de informacion"], [1, "Queja por un producto"], [2, "Felicitaciones"]

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre y Apellido Completo")
    email = models.EmailField(verbose_name="Correo Electronico")
    message = models.TextField( verbose_name="Mensaje")
    contact_type = models.IntegerField(choices=options, verbose_name="Tipo de contacto")
    subscription = models.BooleanField(default=False, verbose_name="Subscribirme a correos informativos")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de envio")

