# Excepciones del Sistema de Libros
class LibroNoEncontradoError(Exception):
    pass

class LibroYaPrestadoError(Exception):
    pass

class LibroNoPrestadoError(Exception):
    pass


# Excepciones del Sistema de Facultad
class MateriaNoEncontradaError(Exception):
    pass

class PersonaNoEncontradaError(Exception):
    pass

class CupoAgotadoError(Exception):
    pass

class EstudianteYaInscriptoError(Exception):
    pass