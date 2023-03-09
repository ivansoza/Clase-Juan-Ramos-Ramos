# Solicitar el valor de radio de un circulo para calcular su area:
# Cálculo del área de un círculo.
from math import pi
r = int(input("Escriba el radio de circulo"))
area = pi*r**2

print("El area del circulo es:{}".format(area))
# Una nueva forma de formatear cadenas en Python 3.6.
print(f"El area del circulo es:{area}")
