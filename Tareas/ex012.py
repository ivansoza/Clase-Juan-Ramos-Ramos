
op=0
lista=["123df","232","233"]



while op !=5:
    if op==1:
        create=int(input("Seleccione por cual manera desea agregar el usuario:\n 1. Metodo Append\n 2. Metodo Extend\n 3. Metodo Insert\n"))
        if create == 1:
            append="S"
            while append != "N":
                acumulador=input("Ingresa el valor que deseas agregar: \n")
                lista.append(acumulador)
                append=input("Deseas agregar otro dato (S/N)")
                append=append.upper()

        elif create==2:
            ext=input("\tAgrega varios valores separado por una (,)\n")
            Lista2=ext.split(",") 
            print(Lista2)
            lista.extend(Lista2)
        elif create ==3:
            for i in range (len(lista)):
                print("Valor {} es: {}".format(i,lista[i]))
            
            insertar=int(input("En que posicion quieres agregar el dato:\n"))
            insertar_dato=input("Cual es el nuevo valor que deseas agregar?\n")
            print("Valor Agregado satisfactoriamente\n")
            input("<<<<<----ENTER PARA CONTINUAR----->>>>>")
            lista.insert(insertar,insertar_dato)
        else:
            print("No elegiste una opcion valida")
    elif op==2:
        for i in range (len(lista)):
                print("Valor {} es: {}".format(i,lista[i]))
    elif op==3:
        for i in range (len(lista)):
                print("Valor {} es: {}".format(i,lista[i]))

        update=int(input("Que valor deseas modificar:\n"))
        update_valor=input("Cual es el nuevo valor.")
        lista[update]=update_valor
        print("Valor modificado")

    elif op==4:
        delete=int(input("Por cual metodo quieres eliminar\n 1. Metodo Remove\n 2. Metodo Pop\n"))
        if delete==1:
            for i in range (len(lista)):
                print("Valor : {}".format(lista[i]))
            delete_valor=input("Que valor deseas eliminar: \n")
            lista.remove(delete_valor)
        elif delete==2:
            lista.pop()
        else:
            print("Opcion Incorrecta")
    

    op=int(input("\tSeleccione que opcion desea hacer: \n 1. Crear\n 2. Leer\n 3. Actualizar\n 4. Eliminar\n 5. Salir\n"))
    
print("\tSaliste del menu")