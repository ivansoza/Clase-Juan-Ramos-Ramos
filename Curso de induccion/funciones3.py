#Argumentos indeterminados en plar clave-valor

def imprimir(**kwargs):
    for kwarg in kwargs:
        print(kwarg, "-->",kwargs[kwarg])

imprimir(dato1="hola",dato2="mundo")
imprimir(diez="10", veinte="20", treinta="30",cuarenta="40")
imprimir(dato1="Arley Ivan",dato2="solis")