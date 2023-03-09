#Programa para Operaciones aritmeticas 

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

num1=int(input("Ingresa el valor de numero 1: "))
num2=int(input("Ingresa el valor de numero 2: "))

def pedir_valor (num1,num2):
    num1= int(input("Dame el valor de Numero 1 "))
    num2= int(input("Dame el valor de Numero 2 "))
    return num1,num2




suma=suma(num1,num2)
print("El resultado es: ",suma)

