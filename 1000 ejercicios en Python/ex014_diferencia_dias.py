#Ejercicio 14: Calcula la diferencia en dias en dos fechas dadas 

from datetime import date

hoy = date(2019, 9, 23)
otra_fecha = date(2022, 11, 16)

delta = otra_fecha - hoy

print(delta)
print(delta.days)