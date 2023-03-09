import os

class Libro(object):
    def __init__(self, id, titulo, autor, edicion,  editorial):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.edicion = edicion
        self.editorial = editorial
 
    def __str__(self):
        return "%s %s %s %s %s" % \
        (self.id, self.titulo, self.autor, self.edicion, self.editorial)
 
    def __getattribute__(self, atrib):
        return object.__getattribute__(self, atrib)
 
class LibroAdmin:
    def __init__(self):
        self.arregLibros = []
 
    def agregar(self, id, titulo, autor, edicion,  editorial):
        libro = Libro(id, titulo, autor, edicion,  editorial)
        self.arregLibros.append(libro)
 
    def buscar(self, clave, por="id"):
        for indice, libro in enumerate(self.arregLibros):
            if libro.__getattribute__(por) == clave:
                return indice
 
    def remover(self, clave, por="id"):
        indice = self.buscar(clave)
        if indice != None:
            self.arregLibros.pop(indice)
            return indice
 
    def __str__(self):
        s = ""
        for libro in self.arregLibros:
            s += str(libro) + '\n'
        return s
 
#Uso de las clases Libro y LibroAdmin:
arreglo = LibroAdmin()
os.system('cls')
op= 'S'
while op == 'S':
    cla= input('Clave del libro:      ')
    tit= input('Cual es el Titulo?:   ')
    aut= input('Nombre del Autor?:    ')
    edi= input('Indica la Edición:    ')
    edt= input('Escribe la Editorial: ')
    arreglo.agregar(cla, tit, aut, edi, edt)    
    op = input('  Desea ingresar mas?    ').upper()

print ('\n')
print(arreglo)

elemento= input('\nElemento a buscar: ')
print('Elemento en posición: ', arreglo.buscar(elemento))

elemento= input('\nElemento a eliminar: ')
print('Se elimina elemento en la posicion: ',arreglo.remover(elemento))

print('\n')
print(arreglo)