from gestion_libros import Libro, Biblioteca
from excepciones import LibroNoEncontradoError, LibroYaPrestadoError

# Creamos la biblioteca una sola vez antes de abrir el menú
mi_biblioteca = Biblioteca("Biblioteca Central")

# Este bucle hace que el programa funcione infinitamente hasta que elijas "Salir"
while True:
    print("\n" + "="*30)
    print("   SISTEMA DE BIBLIOTECA")
    print("="*30)
    print("1. Agregar un libro nuevo")
    print("2. Buscar un libro por ISBN")
    print("3. Prestar un libro")
    print("4. Salir del sistema")
    
    opcion = input("\nElige una opción (1-4): ")
    
    if opcion == "1":
        # Pedimos los datos al usuario
        isbn = input("Ingresa el número ISBN: ")
        titulo = input("Ingresa el título del libro: ")
        autor = input("Ingresa el autor: ")
        
        # Usamos tus clases para crear y guardar el libro
        nuevo_libro = Libro(isbn, titulo, autor)
        mi_biblioteca.agregar_libro(nuevo_libro)
        print(f"¡El libro '{titulo}' fue agregado con éxito!")
        
    elif opcion == "2":
        isbn_buscar = input("Ingresa el ISBN del libro que buscas: ")
        try:
            libro = mi_biblioteca.buscar_libro(isbn_buscar)
            print(f" Libro encontrado: '{libro.titulo}' por {libro.autor}.")
            estado = "Prestado" if libro.prestado else "Disponible en sala"
            print(f"Estado actual: {estado}")
        except LibroNoEncontradoError as error:
            print(f" {error}")
            
    elif opcion == "3":
        isbn_prestar = input("Ingresa el ISBN del libro a prestar: ")
        try:
            mi_biblioteca.prestar_libro(isbn_prestar)
            print(" Libro prestado con éxito. ¡No olvides devolverlo!")
        except (LibroNoEncontradoError, LibroYaPrestadoError) as error:
            # Aquí tu sistema te protege de errores
            print(f" No se pudo prestar: {error}")
            
    elif opcion == "4":
        print("¡NOS RE VIMOS!")
        break  # Esto rompe el bucle y apaga el programa
        
    else:
        print("Opción no válida. Por favor, escribe un número del 1 al 4.")