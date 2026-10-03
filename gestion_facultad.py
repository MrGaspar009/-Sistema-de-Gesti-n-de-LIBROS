class Estudiante:
    def __init__(self, nombre, apellido, matricula, carrera):
        self.nombre = nombre
        self.apellido = apellido
        self.matricula = matricula
        self.carrera = carrera
        self.cursos_inscriptos = []

class Curso:
    def __init__(self, nombre, codigo, profesor, capacidad):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        self.capacidad = int(capacidad)
        self.estudiantes_inscriptos = []

class Facultad:
    def __init__(self):
        self.estudiantes = []
        self.cursos = []

    def agregar_estudiante(self, estudiante):
        if estudiante.matricula == "" or estudiante.nombre == "" or estudiante.apellido == "" or estudiante.carrera == "":
            print("Error: Ningún dato del estudiante puede estar vacío.")
            return
            
        if not estudiante.matricula.isdigit():
            print("Error: La matrícula debe contener solamente números.")
            return

        for est in self.estudiantes:
            if est.matricula == estudiante.matricula:
                print("Error: Ya existe un estudiante con esa matrícula.")
                return

        self.estudiantes.append(estudiante)
        print("Estudiante agregado correctamente.")

    def agregar_curso(self, curso):
        if curso.codigo == "" or curso.nombre == "" or curso.profesor == "":
            print("Error: Ningún dato del curso puede estar vacío.")
            return

        for cur in self.cursos:
            if cur.codigo == curso.codigo:
                print("Error: Ya existe un curso con ese código.")
                return

        self.cursos.append(curso)
        print("Curso agregado correctamente.")

    def inscribir_estudiante(self, matricula, codigo_curso):
        if not matricula.isdigit():
            print("Error: La matrícula debe contener solamente números.")
            return

        estudiante_valido = None
        for est in self.estudiantes:
            if est.matricula == matricula:
                estudiante_valido = est
                break
                
        if estudiante_valido == None:
            print("Error: La matrícula no está registrada.")
            return

        curso_valido = None
        for cur in self.cursos:
            if cur.codigo == codigo_curso:
                curso_valido = cur
                break
                
        if curso_valido == None:
            print("Error: El código de curso no existe.")
            return

        for c in estudiante_valido.cursos_inscriptos:
            if c.codigo == codigo_curso:
                print("Error: El estudiante ya está inscripto en este curso.")
                return
            
        if len(curso_valido.estudiantes_inscriptos) >= curso_valido.capacidad:
            print("Error: No hay cupos disponibles en este curso.")
            return

        curso_valido.estudiantes_inscriptos.append(estudiante_valido)
        estudiante_valido.cursos_inscriptos.append(curso_valido)
        print("Estudiante inscripto correctamente.")

    def baja_curso(self, matricula, codigo_curso):
        if not matricula.isdigit():
            print("Error: La matrícula debe contener solamente números.")
            return

        estudiante_valido = None
        for est in self.estudiantes:
            if est.matricula == matricula:
                estudiante_valido = est
                break
                
        if estudiante_valido == None:
            print("Error: El estudiante no existe.")
            return

        curso_valido = None
        for cur in self.cursos:
            if cur.codigo == codigo_curso:
                curso_valido = cur
                break
                
        if curso_valido == None:
            print("Error: El curso no existe.")
            return

        if curso_valido not in estudiante_valido.cursos_inscriptos:
            print("Error: El estudiante no está inscripto en este curso.")
            return

        estudiante_valido.cursos_inscriptos.remove(curso_valido)
        curso_valido.estudiantes_inscriptos.remove(estudiante_valido)
        print("El estudiante se dio de baja correctamente.")

    def mostrar_cursos(self):
        if len(self.cursos) == 0:
            print("No hay cursos registrados.")
            return

        print("\n----- CURSOS DE LA FACULTAD -----")
        for curso in self.cursos:
            inscriptos = len(curso.estudiantes_inscriptos)
            disponibles = curso.capacidad - inscriptos
            print(f"\nNombre: {curso.nombre}")
            print(f"Código: {curso.codigo}")
            print(f"Profesor: {curso.profesor}")
            print(f"Capacidad máxima: {curso.capacidad}")
            print(f"Estudiantes inscriptos: {inscriptos}")
            print(f"Cupos disponibles: {disponibles}")

    def mostrar_estudiantes(self):
        if len(self.estudiantes) == 0:
            print("No hay estudiantes registrados.")
            return

        print("\n----- ESTUDIANTES DE LA FACULTAD -----")
        for estudiante in self.estudiantes:
            print(f"\nNombre: {estudiante.nombre}")
            print(f"Apellido: {estudiante.apellido}")
            print(f"Matrícula: {estudiante.matricula}")
            print(f"Carrera: {estudiante.carrera}")
            
            if len(estudiante.cursos_inscriptos) == 0:
                print("Cursos inscriptos: Ninguno")
            else:
                print("Cursos inscriptos:")
                for curso in estudiante.cursos_inscriptos:
                    print(f"- {curso.nombre} | Código: {curso.codigo}")

facultad_urquiza = Facultad()

while True:
    print("\nSistema de Gestión de Facultad:")
    print("1- Agregar Estudiante")
    print("2- Agregar Curso")
    print("3- Inscribir Estudiante a Curso")
    print("4- Dar de Baja Estudiante de Curso")
    print("5- Mostrar Cursos")
    print("6- Mostrar Estudiantes")
    print("7- Salir")
    
    opcion = input("\nSeleccione una opción: ")
    
    if opcion == "1":
        nom = input("Ingrese el nombre del estudiante: ")
        ape = input("Ingrese el apellido del estudiante: ")
        mat = input("Ingrese el número de matrícula: ")
        car = input("Ingrese la carrera del estudiante: ")
        facultad_urquiza.agregar_estudiante(Estudiante(nom, ape, mat, car))
            
    elif opcion == "2":
        nom = input("Ingrese el nombre del curso: ")
        cod = input("Ingrese el código del curso: ")
        prof = input("Ingrese el profesor encargado: ")
        cap = input("Ingrese la capacidad máxima de estudiantes: ")
        
        if not cap.isdigit() or int(cap) <= 0:
            print("Error: La capacidad debe ser un número mayor a 0.")
        else:
            facultad_urquiza.agregar_curso(Curso(nom, cod, prof, cap))
            
    elif opcion == "3":
        mat = input("Ingrese la matrícula del estudiante: ")
        cod = input("Ingrese el código del curso: ")
        facultad_urquiza.inscribir_estudiante(mat, cod)

    elif opcion == "4":
        mat = input("Ingrese la matrícula del estudiante: ")
        cod = input("Ingrese el código del curso: ")
        facultad_urquiza.baja_curso(mat, cod)

    elif opcion == "5":
        facultad_urquiza.mostrar_cursos()

    elif opcion == "6":
        facultad_urquiza.mostrar_estudiantes()
            
    elif opcion == "7":
        print("Programa Terminado")
        break
        
    else:
        print("Error: opción no válida.")
        print("Saliendo del sistema...")
        break
        
    else:
        print("Opción incorrecta. Por favor elegí un número del 1 al 6.")
