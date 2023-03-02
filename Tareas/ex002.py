num1 = int(input("Numero 1:"))
num2 = int(input("Numero 2:"))

suma = num1 + num2
resta = num1 - num2
producto = num1 % num2
division = num1/num2


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
