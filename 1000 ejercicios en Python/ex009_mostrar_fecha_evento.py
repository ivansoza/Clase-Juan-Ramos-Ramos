# Mostrar la fecha de un evento almacenada en una tupla

fecha_evento = (2023, 9, 14)

print(type(fecha_evento))
print(fecha_evento)

# Printing the string "El evento programado sera para la fecha:" and the value of the variable
# fecha_evento.
print("El evento programado sera para la fecha:", fecha_evento)
print("El evento programado sera para la fecha: %i/%i/%i" % fecha_evento)
año, mes, dia = fecha_evento
print("El evento programado sera para la fecha: {}/{}/{}".format(año, mes, dia))
