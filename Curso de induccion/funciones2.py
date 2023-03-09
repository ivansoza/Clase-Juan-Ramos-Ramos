#Funciones con argumentos variables (indeterminadas)
import os
def imprimir (*args):
    for argumento in args:
        print(argumento)

#aqui inicia la ejecucion del programa 
os.system("cls")
imprimir(100)
imprimir("Hola","mundo","desde Python")
imprimir("adios")
imprimir(True,False)
imprimir(2.0,2.5,3.4,2.5)