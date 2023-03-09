import os

os.system("cls")

lista=[]
lista.extend([100,200])
print(lista)
input("\t \t Presiona <<enter>> para continuar")

lista.insert(0,3000)
print(lista)
input("\t \t Presiona <<enter>> para continuar")
lista.remove(200)
print(lista)
input("\t \t Presiona <<enter>> para continuar")

lista.pop()
print(lista)
input("\t \t Presiona <<enter>> para continuar")

lista.append(200)
print(lista)
input("\t \t Presiona <<enter>> para continuar")

lista.extend([200,453,235,234,3456])
print(lista)
input("\t \t Presiona <<enter>> para continuar")

#SLICES 
print(lista[0:2])
print(lista[:4])
print(lista[3:])
input("\t Presiona <<enter>> para continuar")

