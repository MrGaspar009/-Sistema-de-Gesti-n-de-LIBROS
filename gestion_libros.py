from excepciones import LibroNoEncontradoError, LibroYaPrestadoError, LibroNoPrestadoError

class Libro:
    def __init__(self, isbn, titulo, autor):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.prestado = False

    def prestar(self):
        if self.prestado:
            raise LibroYaPrestadoError("El libro ya esta prestado.")
        self.prestado = True

    def devolver(self):
        if not self.prestado:
            raise LibroNoPrestadoError("El libro no estaba prestado.")
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
        raise LibroNoEncontradoError("No se encontro el libro con ese ISBN.")

    def prestar_libro(self, isbn):
        libro = self.buscar_libro(isbn)
        libro.prestar()

    def devolver_libro(self, isbn):
        libro = self.buscar_libro(isbn)
        libro.devolver()