# Solicitar al usuario que ingrese un número con 4 dígitos.
num = int(input("Dame un número de 4 cifras: "))

# Comprobando si el número está entre 0 y 9999.
if num > 0 and num <= 9999:
    if num < 10:
        print("Es unidad")
    elif num < 100:
        print("Es decena")
    elif num < 1000:
        print("Es centena")
    else:
        print("Es millar")
else:
    print("Error")