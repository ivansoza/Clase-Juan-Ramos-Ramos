'''
ESCTRUCTURAS DE DATOS EN PYTHON 
*LISTAS (list) [1,2,3], ['1','2','3'], [1.0,2.0,3.0], ['hola',3, True, 6.5]
*TUPLA (tuple)  (0,1,2,3,4,5,6,7,8,9),(0,1),('a','e','i','o','u')
*DICCIONARIOS (dict) {clave=valor}{"3501"="Bartolome", "3502"="Blanca"}
*CONJUNTOS (set -frozenset) set =set (1,2,3,4,5)
                            set2 = {10,20,30,40,50}

'''
import os
lista = [1,2,3], ['1','2','3'], [1.0,2.0,3.0], ['hola',3, True, 6.5]
tupla = (0,1,2,3,4,5,6,7,8,9),(0,1),('a','e','i','o','u')
diccionario = {"3501":"Bartolome", "3502":"Blanca","3503":"Arley Ivan"}
conjunto = set()

os.system ("cls")
print(lista)
print(tupla)
print(diccionario)
print(type(diccionario))
print(type(conjunto))