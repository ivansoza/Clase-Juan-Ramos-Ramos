n=int(input("Ingresa un numero:"))

if n == 1:
    dia= "lunes"
elif n== 2:
    dia="Martes"
elif n== 3:
    dia="Miercoles"
elif n== 4:
    dia="Jueves"
elif n== 5:
    dia="Viernes"
elif n== 6:
    dia="Sabado"
elif n== 7:
    dia="Domingo"
else:
    print("Numero incorrecto") 
print(dia)