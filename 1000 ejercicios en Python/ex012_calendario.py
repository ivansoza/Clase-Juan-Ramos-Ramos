#Ejercicio 12: imprimir el calendario para un año y mes en especifico.

import calendar

agnio = int(input("Escriba el año: "))
mes = int(input("Escriba el mes: "))

print(calendar.month(agnio,mes))