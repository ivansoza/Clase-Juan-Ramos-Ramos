#Diccionarios: Estructura que almacena elementos como
#pares clave-valor

alumnos =dict()
alumnos = {"3501":"Bartolome",
           "3502": "Blanca",
           "3503":"Enrique",
           "3504":"Itzel"
}

print(alumnos)

#Recorridos

for clave, valor in alumnos.items():
    print("{0} --> {1}".format(clave,valor))


#Insertar elementos
alumnos.setdefault("3501","Nuevo Valor")   
print (alumnos)
alumnos.setdefault("3505","Arley")   
print (alumnos)

alumnos["3501"]="Otro valor"
print(alumnos)

print (alumnos["3501"])

matricula= input("Ingresa el numero de la clave del alumno: ")
nombre = input("Ingresa el nombre del alumno: ")
alumnos.setdefault(matricula,nombre)
print(alumnos)

for i in range(3):
    num_matricula = input("Ingrese el número de matrícula del alumno: ")
    nombre = input("Ingrese el nombre del alumno: ")
    alumnos.setdefault(num_matricula,nombre)
    print(alumnos)