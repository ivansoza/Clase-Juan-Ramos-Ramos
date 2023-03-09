#PROGRAMACION ORIENTADA A OBJETOS
#PROGRAMACION ORIENTADA A EVENTOS
#LA POO INTEGRA ATRIBUTOS Y METODOS

class Persona():
    #metodo constructor
    def __init__(self,name,address,hair):
        self.__nombre =name
        self.direccion=address
        self.color_pelo=hair
        
    def color_pelo(self):
        return self.color_pelo

    def __getdireccion(self): #atributo privado
        return self.direccion
    
    def get_nombre(self):
        return (self.__nombre)
    
    def set_nombre (self):
        self.__nombre = input("Nuevo nombre de la persona")

    def pintar_pelo(self, nuevo):
        self.color_pelo =nuevo

#inicio de ejecucion 
objeto1 = Persona("Ana", "Av Zaragoza","Castaño")

print(objeto1.get_nombre())
Persona.set_nombre()

#Tratar de entender este codigo