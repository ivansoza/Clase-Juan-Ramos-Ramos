n1=int(input("Dame un numero: "))
n2=int(input("Dame un numero: "))
op=0
while op !=5:
    print("1: Sumar")
    print("2: Restar")
    print("3: Multiplicacion")
    print("4: Division")
    print("5: Salir")

    op= int(input("Elige la opcion: "))

    if op==1:
        suma=n1+n2
        print("Suma",suma)    
    elif op==2:
        resta=n1-n2
        print("Resta",resta)
    elif op==3:
        multiplicacion=n1*n2
        print("Multiplicacion",multiplicacion)
    elif op==4:
        division=n1/n2
        print("Division", division)
    else:
        print("Numero invalido")
    print("Estas dentro del ciclo:")
print("estas fuera del ciclo")