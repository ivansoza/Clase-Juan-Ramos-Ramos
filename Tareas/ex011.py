#TAREA: DISEÑAR UN PROGRAMA QUE GESTIONE UN DICCIONARIO  CON LAS OPERACIONES CRUD A MANERA DE MENU 

def menu_centro(letra):
    print("\t\t{}\n".format(letra))

def no_es_digito():
    print ("No es un valor numerico, por favor ingresa un valor numerico.")
def fuera_de_rango():
    print ("No es un valor que esta en el rango.")

def imprimir_dic(diccionario):
    menu_centro("DICCIONARIO")
    for k,v in diccionario.items():
        print("Clave: {} Valor: {}".format(k,v))
    print("")


diccionario = {1:"Ivan",2:"Juan"}
clave= max(diccionario.keys())+1 #saber el numero limite y aumentar uno
op="S"
while True:
    menu_centro("Menu")

    menu_str=input("\tSeleccione que opcion desea hacer: \n 1. Crear\n 2. Leer\n 3. Actualizar\n 4. Eliminar\n 5. Salir\n")
    if menu_str.isdigit():
        menu=int(menu_str)
        if(menu>0 and menu <=5):
            if menu==1:
                while op.upper() != "N":
                    valor=input("Valor:\n")
                    diccionario[clave]=valor
                    clave +=1
                    while True:
                        op=input("\t Desea agregar a otro alumno (s)/(n)")
                        op=op.upper()
                        if op=="S" or op=="N":
                             break
                        else:
                            fuera_de_rango()
                        
            elif menu==2:
                imprimir_dic(diccionario)
                input("<<<---Presiona ENTER--->>>")

            elif menu==3:
                menu_centro("UPDATE")
                imprimir_dic(diccionario)
                while True:
                    clave_update_str=input("Cual es la clave que deseas modificar:\n ")
                    if clave_update_str.isdigit():
                        clave_update=int(clave_update_str)
                        if clave_update <= clave:
                            valor=input("Nuevo valor de {}".format(clave_update))
                            diccionario[clave_update]=valor
                            break
                        else: 
                            fuera_de_rango()
                    else:
                        no_es_digito()
                
                
            elif menu==4:
                menu_centro("ELIMINAR")
                imprimir_dic(diccionario)
                while True:
                    clave_delete=input("\tQue clave desea eliminar del diccionario:\n")
                    if clave_delete.isdigit():
                        clave_de=int(clave_delete)
                        if clave_de in diccionario:
                            del diccionario[clave_de]
                            break
                        else:
                            fuera_de_rango()
                    else:
                        no_es_digito()
                
                
            elif menu==5:
                print("Seguro que quieres salir ")
                print("\t\t<<<--SALISTE DEL MENU -->>>")
                break
        else:
            fuera_de_rango()    
    else:
        no_es_digito()