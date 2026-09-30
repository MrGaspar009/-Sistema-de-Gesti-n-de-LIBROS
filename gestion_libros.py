class LibroNoEncontradoError(Exception): pass
class LibroYaPrestadoError(Exception): pass
class SocioNoEncontradoError(Exception): pass

class Libro:
    def __init__(self, isbn, titulo):
        self.isbn = isbn
        self.titulo = titulo
        self.prestado = False

class Socio:
    def __init__(self, numero, nombre):
        self.numero = numero
        self.nombre = nombre

class Biblioteca:
    def __init__(self):
        self.catalogo = []
        self.socios = []

    def agregar_libro(self, libro):
        self.catalogo.append(libro)
        
    def agregar_socio(self, socio):
        self.socios.append(socio)

    def eliminar_libro(self, isbn):
        libro_encontrado = None
        for libro in self.catalogo:
            if libro.isbn == isbn:
                libro_encontrado = libro
                break
                
        if not libro_encontrado:
            raise LibroNoEncontradoError("El ISBN no existe en el catálogo.")
        if libro_encontrado.prestado:
            raise LibroYaPrestadoError("No se puede dar de baja un libro que está prestado.")
            
        self.catalogo.remove(libro_encontrado)

    def eliminar_socio(self, numero_socio):
        socio_encontrado = None
        for socio in self.socios:
            if socio.numero == numero_socio:
                socio_encontrado = socio
                break
                
        if not socio_encontrado:
            raise SocioNoEncontradoError("El número de socio no está registrado.")
            
        self.socios.remove(socio_encontrado)

    def prestar_libro(self, isbn, numero_socio):
        socio_valido = False
        for socio in self.socios:
            if socio.numero == numero_socio:
                socio_valido = True
                break
        if not socio_valido:
            raise SocioNoEncontradoError("El número de socio no está registrado.")

        libro_encontrado = None
        for libro in self.catalogo:
            if libro.isbn == isbn:
                libro_encontrado = libro
                break
                
        if not libro_encontrado:
            raise LibroNoEncontradoError("El ISBN no existe en el catálogo.")
        if libro_encontrado.prestado:
            raise LibroYaPrestadoError("El libro ya se lo llevó otra persona.")
        
        libro_encontrado.prestado = True


# --- 3. PROGRAMA PRINCIPAL ---
mi_biblio = Biblioteca()

while True:
    print("\n- MENÚ DE LA BIBLIOTECA -")
    print("1. Dar de alta un libro")
    print("2. Dar de alta un socio")
    print("3. Prestar un libro")
    print("4. Dar de baja un libro")
    print("5. Dar de baja un socio")
    print("6. Salir del programa")
    
    opcion = input("\nElegí una opción (1-6): ")
    
    if opcion == "1":
        print("\n- ALTA DE LIBRO -")
        isbn_nuevo = input("Ingresá el ISBN: ")
        titulo_nuevo = input("Ingresá el título: ")
        mi_biblio.agregar_libro(Libro(isbn_nuevo, titulo_nuevo))
        print("Libro guardado.")
        
    elif opcion == "2":
        print("\n- ALTA DE SOCIO -")
        num_socio = input("Ingresá el número de socio: ")
        nombre_socio = input("Ingresá el nombre: ")
        mi_biblio.agregar_socio(Socio(num_socio, nombre_socio))
        print("Socio guardado.")
        
    elif opcion == "3":
        print("\n- SECCIÓN DE PRÉSTAMOS -")
        socio_ingresado = input("Número de socio que retira: ")
        isbn_ingresado = input("ISBN del libro a retirar: ")
        
        try:
            mi_biblio.prestar_libro(isbn_ingresado, socio_ingresado)
            print("Éxito: El libro ha sido prestado correctamente.")
        except SocioNoEncontradoError as error:
            print(f"Error de Socio: {error}")
        except LibroNoEncontradoError as error:
            print(f"Error de Búsqueda: {error}")
        except LibroYaPrestadoError as error:
            print(f"Préstamo rechazado: {error}")

    elif opcion == "4":
        print("\n- BAJA DE LIBRO -")
        isbn_baja = input("Ingresá el ISBN del libro a eliminar: ")
        try:
            mi_biblio.eliminar_libro(isbn_baja)
            print("Libro eliminado correctamente del catálogo.")
        except LibroNoEncontradoError as error:
            print(f"Error: {error}")
        except LibroYaPrestadoError as error:
            print(f"Error: {error}")

    elif opcion == "5":
        print("\n- BAJA DE SOCIO -")
        socio_baja = input("Ingresá el número de socio a eliminar: ")
        try:
            mi_biblio.eliminar_socio(socio_baja)
            print("Socio eliminado correctamente del sistema.")
        except SocioNoEncontradoError as error:
            print(f"Error: {error}")
            
    elif opcion == "6":
        print("Saliendo del sistema...")
        break
        
    else:
        print("Opción incorrecta. Por favor elegí un número del 1 al 6.")