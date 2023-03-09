import os
os.system("cls")
alumnos = dict()

opc="S"
while opc.upper() !="N":
    clave= input("Clave del alumno: ")
    valor= input("Nombre: ")
    alumnos.setdefault(clave,valor)
    opc=input("\t Desea agregar a otro alumno (s)/(n)")

for k,v in alumnos.items():
    print ("{}==>{}".format(k,v))

input ("\n Presione enter para finalizar")

print("Numero de elementos= ",len(alumnos))
print("Listado de claves: ",alumnos.keys())
print("Listado de claves: ",alumnos.values())
#Obtener valor en una cierta claves 

valor =alumnos.get("1")
print("valor con clave {}={}".format("1",valor))
print("Valor con clave {}".format(alumnos["1"]))

#Eliminar un elemento 
clave=input("Clave a eliminar:")
alumnos.pop(clave)
for k,v in alumnos.items():
    print ("{}==>{}".format(k,v))

#TAREA: DISEÑAR UN PROGRAMA QUE GESTIONE UNA LISTA CON LAS OPERACIONES CRUD A MANERA DE MENU 

#MISMAS FUNCIONES PARA UN DICCIONARIO 

