#Programa para Operaciones aritmeticas 

def leer_dato():
   
    while True:
        resultado= input("Dame el valor de Numero 1 ")
        if resultado.isdigit():
            resultado=int(resultado)
            break
        else:
            print("Porfavor ingresa un numero entero")
    
    return resultado


def suma(n1,n2):
    resultado=n1+n2
    print("Suma: ",resultado)
def resta(n1,n2):
    resultado=n1-n2
    print("Resta: ",resultado)

def multiplicar(n1,n2):
    resultado=n1*n2
    print("Multiplicar: ",resultado)
def dividir(n1,n2):
    resultado=n1/n2
    print("Dividir: ",resultado)

num1=leer_dato()
num2=leer_dato()
import os
os.system("cls")
op=0
while op!=5:
    op=int(input("Operaciones: \n 1. Suma\n 2. Resta\n 3. Multiplicacion\n 4. Division\n 5. Salir\n"))
    if op==1:
        suma(num1,num2)
    elif op==2:
        resta(num1,num2)

    elif op==3:
        multiplicar(num1,num2)
    elif op==4:
        dividir(num1,num2)
    else:
        print("Introduciste un valor incorrecto ")

input("Saliendo del programa PRESIONA ENTER ")

