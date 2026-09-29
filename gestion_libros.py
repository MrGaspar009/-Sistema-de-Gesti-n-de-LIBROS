from excepciones import LibroNoEncontradoError, LibroYaPrestadoError, LibroNoPrestadoError

class Libro:
    def __init__(self, isbn, titulo, autor):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.prestado = False

    def prestar(self):
        if self.prestado:
            raise LibroYaPrestadoError(f"El libro '{self.titulo}' ya está prestado.")
        self.prestado = True

    def devolver(self):
        if not self.prestado:
            raise LibroNoPrestadoError(f"El libro '{self.titulo}' no estaba prestado.")
        self.prestado = False

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo = []

    def agregar_libro(self, libro):
        self.catalogo.append(libro)

    def buscar_libro(self, isbn):
        for libro in self.catalogo:
            if libro.isbn == isbn:
                return libro
        raise LibroNoEncontradoError(f"No se encontró el libro con ISBN: {isbn}.")

    def prestar_libro(self, isbn):
        libro = self.buscar_libro(isbn)
        libro.prestar()

    def devolver_libro(self, isbn):
        libro = self.buscar_libro(isbn)
        libro.devolver()