#TAREA: DISEÑAR UN PROGRAMA QUE GESTIONE UNA LISTA CON LAS OPERACIONES CRUD A MANERA DE MENU 

#MISMAS FUNCIONES PARA UN DICCIONARIO 
import os

os.system("cls")
op=0
lista=["123df","232","233"]

def no_es_digito():
    print ("No es un valor numerico, por favor ingresa un valor numerico.")
def fuera_de_rango():
    print ("No es un valor que esta en el rango.")

def imprimir_lista(lista):
    print("\tLISTA")
    for i in range(len(lista)):
        print("\t\tValor [{}] = [{}]".format(i,lista[i]))

while True:
    menu_str=input("\tSeleccione que opcion desea hacer: \n 1. Crear\n 2. Leer\n 3. Actualizar\n 4. Eliminar\n 5. Salir\n")
    if menu_str.isdigit():
        menu=int(menu_str)
        if menu >0 and menu <=5:
            if menu==1:
                print("\t \tCREAR")
                while True:
                    crear_str=input("\t Seleccione por cual opcion desea crear valores en la lista:\n 1. Uno en uno\n 2. Extend\n 3. Insert\n  ")
                    if crear_str.isdigit():
                        crear=int(crear_str)
                        if crear > 0 and crear <=3:
                            if crear==1:
                                print("\t UNO EN UNO ")
                                while True:
                                    uno_str=input("Cuantos datos deseas agregar:")
                                    try:
                                        uno=int(uno_str)
                                        for i in range(uno):
                                            valor=input("{}: ".format(i))
                                            lista.append(valor)
                                        break
                                    except ValueError:
                                        no_es_digito()
                                break
                            elif crear==2:
                                print("\t EXTEND ")
                                listaex=input("Ingresa los datos con separados por (,)")
                                lista2=listaex.split(",")
                                lista.extend(lista2)
                                break
                            elif crear==3:
                                print("\t INSERT ")
                                imprimir_lista(lista)
                                while True:
                                    insert_str=input("En que posicion deseas agregar el valor: ")
                                    if insert_str.isdigit():
                                        insert=int(insert_str)
                                        if insert <= len(lista):
                                            insert_valor=input("Escribe el valor a agregar:\n ")
                                            lista.insert(insert,insert_valor)
                                            break
                                        else:
                                            fuera_de_rango()
                                    else:
                                        no_es_digito()    
                                
                                break
                        else:
                            fuera_de_rango()

                    else:
                        no_es_digito()
            elif menu==2:
                imprimir_lista(lista)
            elif menu==3:
                print("\t UPDATE ")
                imprimir_lista(lista)
                while True:
                    update_str=input("Que numero de valor desea modificar: \n")
                    if update_str.isdigit():
                        update=int(update_str)
                        if update <= len(lista):
                            new_valor=input("Cual es el nuevo valor?= \n")
                            lista[update]=new_valor
                            break
                        else:
                            fuera_de_rango()
                    else:
                     no_es_digito()
                
                
            elif menu==4:
                print("\tELIMINAR")
                while True:
                    delete_str=input("Por cual metodo desea eliminar:\n 1. Seleccionar\n 2. POP\n")
                    if delete_str.isdigit():
                        delete=int(delete_str)
                        if delete > 0 and delete <=2:
                            if delete==1:
                                print("\t ELIMINACION POR SELECCION")
                                if len(lista)>0:    
                                    imprimir_lista(lista)        
                                    while True:
                                        sele_str=input("Que numero de valor deseas eliminar?\n")
                                        if sele_str.isdigit():
                                            seleccion=int(sele_str)
                                            if seleccion <= len(lista):
                                                lista.pop(seleccion)
                                                break
                                            else:
                                                fuera_de_rango()
                                        else:
                                            no_es_digito()
                                    break
                                else:
                                    print("La lista esta vacia")
                                    break
                            elif delete==2:
                                print("\t ELIMINACION POR POP")
                                if len(lista)>0:
                                    lista.pop()
                                    break
                                else:
                                    print("*La lista esta vacia")
                            break
                                

                        else:
                            fuera_de_rango()
                    else:
                        no_es_digito()
            elif menu==5:
                print("\n\t\tADIOS")
                break
        else:
            fuera_de_rango()
    else:
        no_es_digito()

    

