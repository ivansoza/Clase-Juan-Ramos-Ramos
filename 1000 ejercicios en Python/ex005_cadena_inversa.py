#Obtener la representacion inversa de una cadena de caracteres

#python=> nohtyp

cadena="python"

# Iterando a través de la cadena en orden inverso.
for i in range(len(cadena)-1,-1, -1):
    print(cadena[i],end="")

print()
print(cadena[:])
print(cadena[::-1])


