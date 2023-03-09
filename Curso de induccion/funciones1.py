#programa de operaciones aritmeticas basicas
import os

def sumar(valor1,valor2):
    result = valor1+valor2
    #for i in range(10):
    #    print("Hola")
    return result
def restar(valor1,valor2):
    result =valor1-valor2
    return result
def producto(valor1,valor2):
    return valor1*valor2
def division(valor1,valor2):
    return valor1/valor2

#aqui inicia la ejecucion del programa
os.system("cls")
n1=int(input("Dame el valor 1:"))
n2=int(input("Dame el valor 2:"))
resultado= sumar(n1,n2)
resultado2= restar(n1,n2)
print("EL resultado de la suma ", resultado)
print("EL resultado de la resta de los valores = {0}".format(restar(n1,n2)))
print("EL resultado del producto de los valores = {0}".format(producto(n1,n2)))
print("La division de los valores = {0}".format(division(n1,n2)))


