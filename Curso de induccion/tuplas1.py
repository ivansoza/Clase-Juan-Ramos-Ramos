#Tuplas
vocales = ('a','e','i','o','u')
print (vocales)


misVocales = list(vocales)
print(misVocales)
for i in range (2):
    datonuevo = input("Ingresa el nuevo valor: ")
    misVocales.append(datonuevo)

print (misVocales)
vocales = tuple(misVocales)
print (vocales)

for i in range (0,len(vocales)):
    print (vocales[i])