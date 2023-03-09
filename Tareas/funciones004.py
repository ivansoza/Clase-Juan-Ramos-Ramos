#Funciones con argumentos indeterminados 
lista=[]

def indeterminados (*args):
    for arg in args:
        lista.append(arg)
        print(type(arg))
        print (arg)

indeterminados(4,2.0,"Hola",["Hola",30])


print(lista)

#Funciones con lista de argumentos indeterminados 
#en par clave-valor

def indeterminados_nombre(**kwargs):
    for i in kwargs:
        print(i,"=>",kwargs[i])
    


ola=indeterminados_nombre(n=2,c="Hola",l=[1,2,3,4,4])

