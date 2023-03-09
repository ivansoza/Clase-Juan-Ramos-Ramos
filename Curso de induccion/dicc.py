midict = dict()
n=int(input("Ingresa cuantos usuarios quieres agregar:"))

for i in range(n):
    clave = input("Ingrese el número de matrícula del alumno: ")
    valor = input("Ingrese el nombre del alumno: ")
    midict.setdefault(clave,valor)
    print(midict)

for clave,valor in midict.items():
    print("{0}-->{1}".format(clave,valor))