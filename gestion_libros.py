class Miembro:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre
        self.libros_prestados = []

class Libro:
    def __init__(self, titulo, autor, isbn, ejemplares):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.ejemplares = int(ejemplares)
        self.prestado_a = []

    def esta_disponible(self):
        return len(self.prestado_a) < self.ejemplares

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.miembros = []

    def buscar_libro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None

    def buscar_miembro(self, dni):
        for miembro in self.miembros:
            if miembro.dni == dni:
                return miembro
        return None

    def agregar_libro(self, titulo, autor, isbn, ejemplares):
        if titulo == "" or autor == "" or isbn == "":
            print("Error: Ningún dato del libro puede estar vacío.")
            return

        if not isbn.isdigit():
            print("Error: El ISBN debe contener solamente números.")
            return

        if not ejemplares.isdigit() or int(ejemplares) <= 0:
            print("Error: Debe ingresar una cantidad de ejemplares mayor a 0.")
            return

        cant = int(ejemplares)
        libro_existente = self.buscar_libro(isbn)

        if libro_existente:
            libro_existente.ejemplares += cant
            print("Ejemplares agregados correctamente al libro existente.")
        else:
            nuevo_libro = Libro(titulo, autor, isbn, cant)
            self.libros.append(nuevo_libro)
            print("Libro agregado correctamente.")

    def quitar_libro(self, isbn, cantidad):
        if not isbn.isdigit():
            print("Error: El ISBN debe contener solamente números.")
            return

        if not cantidad.isdigit() or int(cantidad) <= 0:
            print("Error: La cantidad a quitar debe ser un número mayor a 0.")
            return

        libro = self.buscar_libro(isbn)
        if libro is None:
            print("Error: El libro no existe.")
            return

        cant = int(cantidad)
        disponibles = libro.ejemplares - len(libro.prestado_a)

        if cant > disponibles:
            print("Error: No puede quitar tantos ejemplares.")
            print(f"Ejemplares disponibles para quitar: {disponibles}")
            return

        if cant == libro.ejemplares:
            self.libros.remove(libro)
            print("Libro eliminado correctamente.")
        else:
            libro.ejemplares -= cant
            print(f"Ejemplares eliminados correctamente. Quedan {libro.ejemplares} ejemplares.")

    def agregar_miembro(self, miembro):
        if miembro.nombre == "" or miembro.dni == "":
            print("Error: Ningún dato del miembro puede estar vacío.")
            return

        if not miembro.dni.isdigit() or len(miembro.dni) < 6:
            print("Error: El DNI debe contener solamente números y tener al menos 6 dígitos.")
            return

        if self.buscar_miembro(miembro.dni) is not None:
            print("Error: Ya existe un miembro registrado con ese DNI.")
            return

        self.miembros.append(miembro)
        print("Miembro agregado correctamente.")

    def quitar_miembro(self, dni):
        if not dni.isdigit():
            print("Error: El DNI debe contener solamente números.")
            return

        miembro = self.buscar_miembro(dni)
        if miembro is None:
            print("Error: El miembro no existe.")
            return

        if len(miembro.libros_prestados) > 0:
            print("Error: No se puede borrar un miembro que tiene libros prestados.")
            return

        self.miembros.remove(miembro)
        print("Miembro eliminado correctamente.")

    def prestar_libro(self, dni, isbn):
        if not dni.isdigit():
            print("Error: El DNI debe contener solamente números.")
            return

        if not isbn.isdigit():
            print("Error: El ISBN debe contener solamente números.")
            return

        miembro = self.buscar_miembro(dni)
        if miembro is None:
            print("Error: El miembro no existe.")
            return

        libro = self.buscar_libro(isbn)
        if libro is None:
            print("Error: El libro no existe.")
            return

        if not libro.esta_disponible():
            print("Error: No hay ejemplares disponibles de este libro.")
            return

        libro.prestado_a.append(miembro)
        miembro.libros_prestados.append(libro)
        print("Libro prestado correctamente.")

    def devolver_libro(self, dni, isbn):
        if not dni.isdigit():
            print("Error: El DNI debe contener solamente números.")
            return

        if not isbn.isdigit():
            print("Error: El ISBN debe contener solamente números.")
            return

        miembro = self.buscar_miembro(dni)
        if miembro is None:
            print("Error: El miembro no existe.")
            return

        libro = self.buscar_libro(isbn)
        if libro is None:
            print("Error: El libro no existe.")
            return

        if miembro not in libro.prestado_a:
            print("Error: Este miembro no tiene prestado ese libro.")
            return

        libro.prestado_a.remove(miembro)
        miembro.libros_prestados.remove(libro)
        print("Libro devuelto correctamente.")

    def mostrar_libros(self):
        if len(self.libros) == 0:
            print("No hay libros registrados.")
            return

        print("\n----- LIBROS DE LA BIBLIOTECA -----")
        for libro in self.libros:
            disponibles = libro.ejemplares - len(libro.prestado_a)
            print(f"\nTítulo: {libro.titulo}")
            print(f"Autor: {libro.autor}")
            print(f"ISBN: {libro.isbn}")
            print(f"Cantidad de ejemplares: {libro.ejemplares}")
            print(f"Ejemplares disponibles: {disponibles}")

            if len(libro.prestado_a) == 0:
                print("Estado: Disponible")
            else:
                print("Estado: Hay ejemplares prestados.")
                for m in libro.prestado_a:
                    print(f"  - Prestado a: {m.nombre} | DNI: {m.dni}")

    def mostrar_miembros(self):
        if len(self.miembros) == 0:
            print("No hay miembros registrados.")
            return

        print("\n----- MIEMBROS DE LA BIBLIOTECA -----")
        for miembro in self.miembros:
            print(f"\nNombre: {miembro.nombre}")
            print(f"DNI: {miembro.dni}")
            if len(miembro.libros_prestados) == 0:
                print("Libros prestados: Ninguno")
            else:
                print("Libros prestados:")
                for l in miembro.libros_prestados:
                    print(f"  - {l.titulo} | ISBN: {l.isbn}")

    def mostrar_libros_prestados_miembro(self, dni):
        if not dni.isdigit():
            print("Error: El DNI debe contener solamente números.")
            return

        miembro = self.buscar_miembro(dni)
        if miembro is None:
            print("Error: El miembro no existe.")
            return

        print("\n----- LIBROS PRESTADOS -----")
        print(f"Miembro: {miembro.nombre}")
        print(f"DNI: {miembro.dni}")

        if len(miembro.libros_prestados) == 0:
            print("Este miembro no tiene libros prestados.")
        else:
            for libro in miembro.libros_prestados:
                print(f"  - {libro.titulo} | ISBN: {libro.isbn}")

biblioteca_urquiza = Biblioteca()

while True:
    print("\nSistema de Gestión de Biblioteca:")
    print("1- Agregar Libro")
    print("2- Quitar Libro")
    print("3- Agregar Miembro")
    print("4- Borrar Miembro")
    print("5- Prestar Libro")
    print("6- Devolver Libro")
    print("7- Mostrar Libros")
    print("8- Mostrar Miembros")
    print("9- Mostrar Libros Prestados a Miembro")
    print("10- Salir")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        tit = input("Ingrese el título del libro: ")
        aut = input("Ingrese el autor del libro: ")
        isb = input("Ingrese el ISBN del libro: ")
        cant = input("Cuántos ejemplares desea agregar: ")
        biblioteca_urquiza.agregar_libro(tit, aut, isb, cant)

    elif opcion == "2":
        isb = input("Ingrese el ISBN del libro a quitar: ")
        cant = input("Cuántos ejemplares desea quitar: ")
        biblioteca_urquiza.quitar_libro(isb, cant)

    elif opcion == "3":
        nom = input("Ingrese el nombre del socio: ")
        dni = input("Ingrese el DNI del socio: ")
        biblioteca_urquiza.agregar_miembro(Miembro(dni, nom))

    elif opcion == "4":
        dni = input("Ingrese el DNI de la persona a borrar: ")
        biblioteca_urquiza.quitar_miembro(dni)

    elif opcion == "5":
        dni = input("Ingrese el DNI de la persona a la que se le prestará: ")
        isb = input("Ingrese el ISBN del libro a prestar: ")
        biblioteca_urquiza.prestar_libro(dni, isb)

    elif opcion == "6":
        dni = input("Ingrese el DNI de la persona que devuelve el libro: ")
        isb = input("Ingrese el ISBN del libro a devolver: ")
        biblioteca_urquiza.devolver_libro(dni, isb)

    elif opcion == "7":
        biblioteca_urquiza.mostrar_libros()

    elif opcion == "8":
        biblioteca_urquiza.mostrar_miembros()

    elif opcion == "9":
        dni = input("Ingrese el DNI del miembro: ")
        biblioteca_urquiza.mostrar_libros_prestados_miembro(dni)

    elif opcion == "10":
        print("Programa Terminado")
        break

    else:
        print("Error: opción no válida.")
