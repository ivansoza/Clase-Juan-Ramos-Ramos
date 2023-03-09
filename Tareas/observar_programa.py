import os  # Importa el módulo os

# Define la clase Libro
class Libro(object):
    # Constructor de la clase Libro
    def __init__(self, id, titulo, autor, edicion, editorial):
        # Inicializa los atributos del objeto
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.edicion = edicion
        self.editorial = editorial
 
    # Define el método para imprimir un objeto de la clase Libro como una cadena
    def __str__(self):
        return "%s %s %s %s %s" %\
            (self.id, self.titulo, self.autor, self.edicion, self.editorial)
 
    # Define el método para acceder a los atributos del objeto
    def __getattribute__(self, atrib):
        return object.__getattribute__(self, atrib)

# Define la clase LibroAdmin
class LibroAdmin:
    # Constructor de la clase LibroAdmin
    def __init__(self):
        # Inicializa la lista de libros
        self.arregLibros = []
 
    # Define el método para agregar un libro a la lista
    def agregar(self, id, titulo, autor, edicion, editorial):
        # Crea un objeto de la clase Libro y lo agrega a la lista
        libro = Libro(id, titulo, autor, edicion, editorial)
        self.arregLibros.append(libro)
 
    # Define el método para buscar un libro en la lista
    def buscar(self, clave, por="id"):
        # Recorre la lista de libros y busca un libro con el atributo indicado
        for indice, libro in enumerate(self.arregLibros):
            if libro.__getattribute__(por) == clave:
                return indice
 
    # Define el método para remover un libro de la lista
    def remover(self, clave, por="id"):
        # Busca el libro en la lista y lo remueve
        indice = self.buscar(clave)
        if indice != None:
            self.arregLibros.pop(indice)
            return indice
 
    # Define el método para imprimir la lista de libros como una cadena
    def __str__(self):
        s = ""
        for libro in self.arregLibros:
            s += str(libro) + '\n'
        return s

# Crea un objeto de la clase LibroAdmin
arreglo = LibroAdmin()

# Limpia la pantalla
os.system('cls')

# Pide al usuario ingresar información de libros
op = 'S'
while op == 'S':
    cla = input('Clave del libro:      ')
    tit = input('Cual es el Titulo?:   ')
    aut = input('Nombre del Autor?:    ')
    edi = input('Indica la Edición:    ')
    edt = input('Escribe la Editorial: ')
    arreglo.agregar(cla, tit, aut, edi, edt)
    op = input('  Desea ingresar mas?    ').upper()

# Imprime la lista de libros ingresados
print ('\n')
print(arreglo)

# Pide al usuario un elemento para buscar en la lista
elemento = input('\nElemento a buscar: ')
print('Elemento en posición: ', arreglo.buscar(elemento))

# Pide al usuario un elemento para eliminar de la lista
elemento = input('\nElemento a eliminar: ')
print('Se elimina elemento en la posicion: ',arreglo.remover(elemento))
print('\n')
print(arreglo)  