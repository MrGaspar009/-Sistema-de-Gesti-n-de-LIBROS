class DatoVacioError(Exception): pass
class EstudianteNoEncontradoError(Exception): pass
class MateriaNoEncontradaError(Exception): pass
class EstudianteYaInscriptoError(Exception): pass

class Estudiante:
    def __init__(self, legajo, nombre):
        self.legajo = legajo
        self.nombre = nombre
        self.materias_inscriptas = []

class Materia:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

class Facultad:
    def __init__(self):
        self.estudiantes = []
        self.materias = []

    def agregar_estudiante(self, estudiante):
        if estudiante.legajo == "" or estudiante.nombre == "":
            raise DatoVacioError("El legajo y el nombre no pueden estar vacíos.")
        self.estudiantes.append(estudiante)
        
    def agregar_materia(self, materia):
        if materia.codigo == "" or materia.nombre == "":
            raise DatoVacioError("El código y el nombre no pueden estar vacíos.")
        self.materias.append(materia)

    def eliminar_estudiante(self, legajo):
        estudiante_encontrado = None
        for estudiante in self.estudiantes:
            if estudiante.legajo == legajo:
                estudiante_encontrado = estudiante
                break
                
        if not estudiante_encontrado:
            raise EstudianteNoEncontradoError("El legajo no está registrado.")
            
        self.estudiantes.remove(estudiante_encontrado)

    def eliminar_materia(self, codigo):
        materia_encontrada = None
        for materia in self.materias:
            if materia.codigo == codigo:
                materia_encontrada = materia
                break
                
        if not materia_encontrada:
            raise MateriaNoEncontradaError("El código de materia no existe.")
            
        self.materias.remove(materia_encontrada)

    def inscribir_estudiante(self, legajo, codigo_materia):
        # 1. Validar estudiante
        estudiante_valido = None
        for estudiante in self.estudiantes:
            if estudiante.legajo == legajo:
                estudiante_valido = estudiante
                break
        if not estudiante_valido:
            raise EstudianteNoEncontradoError("El legajo no está registrado.")

        materia_valida = False
        for materia in self.materias:
            if materia.codigo == codigo_materia:
                materia_valida = True
                break
        if not materia_valida:
            raise MateriaNoEncontradaError("El código de materia no existe.")

        if codigo_materia in estudiante_valido.materias_inscriptas:
            raise EstudianteYaInscriptoError("El alumno ya se encuentra inscripto en esta materia.")
        
        estudiante_valido.materias_inscriptas.append(codigo_materia)


mi_facu = Facultad()

while True:
    print("\n- MENÚ DE LA FACULTAD -")
    print("1. Dar de alta un estudiante")
    print("2. Dar de alta una materia")
    print("3. Inscribir estudiante a materia")
    print("4. Dar de baja un estudiante")
    print("5. Dar de baja una materia")
    print("6. Salir del programa")
    
    opcion = input("\nElegí una opción (1-6): ")
    
    if opcion == "1":
        print("\n- ALTA DE ESTUDIANTE -")
        legajo_nuevo = input("Ingresá el legajo: ")
        nombre_nuevo = input("Ingresá el nombre: ")
        try:
            mi_facu.agregar_estudiante(Estudiante(legajo_nuevo, nombre_nuevo))
            print("Estudiante guardado.")
        except DatoVacioError as error:
            print(f"Error de Datos: {error}")
            
    elif opcion == "2":
        print("\n- ALTA DE MATERIA -")
        cod_mat = input("Ingresá el código de materia (ej. MAT1): ")
        nom_mat = input("Ingresá el nombre de la materia: ")
        try:
            mi_facu.agregar_materia(Materia(cod_mat, nom_mat))
            print("Materia guardada.")
        except DatoVacioError as error:
            print(f"Error de Datos: {error}")
            
    elif opcion == "3":
        print("\n- INSCRIPCIÓN -")
        legajo_ingresado = input("Legajo del estudiante: ")
        codigo_ingresado = input("Código de la materia: ")
        try:
            mi_facu.inscribir_estudiante(legajo_ingresado, codigo_ingresado)
            print("Éxito: Estudiante inscripto correctamente.")
        except EstudianteNoEncontradoError as error:
            print(f"Error de Estudiante: {error}")
        except MateriaNoEncontradaError as error:
            print(f"Error de Materia: {error}")
        except EstudianteYaInscriptoError as error:
            print(f"Inscripción rechazada: {error}")

    elif opcion == "4":
        print("\n- BAJA DE ESTUDIANTE -")
        legajo_baja = input("Ingresá el legajo del estudiante a eliminar: ")
        try:
            mi_facu.eliminar_estudiante(legajo_baja)
            print("Estudiante eliminado correctamente.")
        except EstudianteNoEncontradoError as error:
            print(f"Error: {error}")

    elif opcion == "5":
        print("\n- BAJA DE MATERIA -")
        mat_baja = input("Ingresá el código de la materia a eliminar: ")
        try:
            mi_facu.eliminar_materia(mat_baja)
            print("Materia eliminada correctamente.")
        except MateriaNoEncontradaError as error:
            print(f"Error: {error}")
            
    elif opcion == "6":
        print("Saliendo del sistema...")
        break
        
    else:
        print("Opción incorrecta. Por favor elegí un número del 1 al 6.")