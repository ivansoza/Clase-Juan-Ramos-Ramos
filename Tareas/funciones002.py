#Programa para Operaciones aritmeticas 

def leer_dato():
    resultado= int(input("Dame el valor de Numero 1 "))
    return resultado


def suma(n1,n2):
    resultado=n1+n2
    return resultado
def resta(n1,n2):
    resultado=n1-n2
    return resultado
def multiplicar(n1,n2):
    resultado=n1*n2
    return resultado
def dividir(n1,n2):
    resultado=n1/n2
    return resultado

num1=leer_dato()
num2=leer_dato()
import os
os.system("cls")
op=0
while op!=5:
    op=int(input("Operaciones: \n 1. Suma\n 2. Resta\n 3. Multiplicacion\n 4. Division\n 5. Salir\n"))
    if op==1:
        suma=suma(num1,num2)
        print("Suma: {}".format(suma))
    elif op==2:
        resta=resta(num1,num2)
        print("Resta: {}".format(resta))
    elif op==3:
        multiplicacion=multiplicar(num1,num2)
        print("Multiplicacion: {}".format(multiplicacion))
    elif op==4:
        division=dividir(num1,num2)
        print("Division: {}".format(division))
    else:
        print("Introduciste un valor incorrecto ")

input("Saliendo del programa PRESIONA ENTER ")





#2 




