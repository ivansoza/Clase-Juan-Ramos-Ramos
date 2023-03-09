#CAPTURAR DATOS DE UNA LISTA, uno a uno #

L1=[1,3,4,5,6] #Lista Vacia
print(L1)
n=int(input("Cuantos datos nuevos quieres ingresar a la lista:?"))
print(L1)
for i in range(n):
    dato=int(input("Valor {0}: ".format(i)))
    print (L1)
    L1.extend([dato])

print (L1)