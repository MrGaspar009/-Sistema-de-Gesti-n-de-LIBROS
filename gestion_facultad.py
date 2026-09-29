from excepciones import MateriaNoEncontradaError, PersonaNoEncontradaError, CupoAgotadoError, EstudianteYaInscriptoError

class Persona:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre

class Estudiante(Persona):
    def __init__(self, dni, nombre, legajo):
        super().__init__(dni, nombre)
        self.legajo = legajo

class Materia:
    def __init__(self, codigo, nombre, cupo_maximo):
        self.codigo = codigo
        self.nombre = nombre
        self.cupo_maximo = cupo_maximo
        self.estudiantes = []

    def inscribir_estudiante(self, estudiante):
        if estudiante in self.estudiantes:
            raise EstudianteYaInscriptoError(f"{estudiante.nombre} ya está inscripto.")
        if len(self.estudiantes) >= self.cupo_maximo:
            raise CupoAgotadoError(f"No hay cupos en {self.nombre}.")
        self.estudiantes.append(estudiante)

class Facultad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.materias = []
        self.estudiantes = []

    def agregar_materia(self, materia):
        self.materias.append(materia)

    def registrar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def buscar_estudiante(self, legajo):
        for est in self.estudiantes:
            if est.legajo == legajo:
                return est
        raise PersonaNoEncontradaError("Estudiante no encontrado.")

    def buscar_materia(self, codigo):
        for mat in self.materias:
            if mat.codigo == codigo:
                return mat
        raise MateriaNoEncontradaError("Materia no encontrada.")

    def inscribir_estudiante_en_materia(self, legajo, codigo_materia):
        estudiante = self.buscar_estudiante(legajo)
        materia = self.buscar_materia(codigo_materia)
        materia.inscribir_estudiante(estudiante)