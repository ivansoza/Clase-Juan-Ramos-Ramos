# El código  le pide al usuario que ingrese un número, luego agrega el número a sí mismo dos
# veces y luego suma los tres números.

#n= 3 3+33+333= 369
n = input("Escriba el valor de n: ")

nn = int("{}{}".format(n,n))
nnn = int("%s%s%s"%(n,n,n))
n = int(n)
suma = n + nn + nnn

print(f"El resultado es: {suma}")