#Estas son las exepsiones, los errores que pueden pasar
class LibroNoEncontradoError(Exception): pass
class LibroYaPrestadoError(Exception): pass
class LibroNoPrestadoError(Exception): pass
class MateriaNoEncontradaError(Exception): pass
class PersonaNoEncontradaError(Exception): pass
class CupoAgotadoError(Exception): pass
class EstudianteYaInscriptoError(Exception): pass