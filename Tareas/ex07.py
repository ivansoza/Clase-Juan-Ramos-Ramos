lista = []
opc = "S"

while opc != "N":
    dato = int(input("Ingresa un número: "))
    lista.append(dato)
    opc = input("\nDeseas ingresar más datos? (S/N)").upper()

for i in range(len(lista)):
    print(lista[i])
