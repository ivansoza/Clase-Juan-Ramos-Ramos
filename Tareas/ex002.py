# Le pide al usuario que ingrese un número y luego lo almacena en la variable num1 y num2.
num1 = int(input("Numero 1:"))
num2 = int(input("Numero 2:"))

suma = num1 + num2
resta = num1 - num2
producto = num1 % num2
division = num1/num2


# Imprimiendo la suma, el resto y el producto de los dos números.
print("Suma= {} \nResta: {}\nProducto:{}".format(suma, resta, producto))

if num1 > num2:
    print("el primer numero es mayor ")
elif num2 > num1:
    print("El segundo es mayor")
else:
    print("son iguales")

if num1 >= 0:
    print("Positivo")
else:
    print("Negativo")
