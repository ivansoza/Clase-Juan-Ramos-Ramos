
# Imprimiendo la fecha y hora actual.
import datetime

ahora = datetime.datetime.now()

print(ahora)

print(type(ahora))

# Impresión de la fecha y la hora en un formato específico.
print(ahora.strftime("%d/%m/%Y %H:%M:%S"))