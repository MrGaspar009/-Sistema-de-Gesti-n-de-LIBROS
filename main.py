from gestion_libros import Biblioteca, Libro
from gestion_facultad import Facultad, Materia, Estudiante
from excepciones import *

print("=== PRUEBAS SISTEMA DE LIBROS ===")
biblio = Biblioteca("Biblioteca Central")
libro1 = Libro("101", "Python Basico", "Guido Rossum")
biblio.agregar_libro(libro1)

# Prueba 1: Libro no encontrado
try:
    biblio.prestar_libro("999")
except LibroNoEncontradoError as e:
    print("Error atrapado:", e)

# Prueba 2: Prestar y re-prestar
biblio.prestar_libro("101")
try:
    biblio.prestar_libro("101")
except LibroYaPrestadoError as e:
    print("Error atrapado:", e)

# Prueba 3: Devolver y re-devolver
biblio.devolver_libro("101")
try:
    biblio.devolver_libro("101")
except LibroNoPrestadoError as e:
    print("Error atrapado:", e)


print("\n=== PRUEBAS SISTEMA DE FACULTAD ===")
facu = Facultad("Facultad Tecno")
materia1 = Materia("M01", "Programacion 1", 1)
facu.agregar_materia(materia1)

e1 = Estudiante("11111111", "Carlos", "E01")
e2 = Estudiante("22222222", "Ana", "E02")
facu.registrar_estudiante(e1)
facu.registrar_estudiante(e2)

# Prueba 1: Estudiante no registrado
try:
    facu.inscribir_estudiante_en_materia("E99", "M01")
except PersonaNoEncontradaError as e:
    print("Error atrapado:", e)

# Prueba 2: Materia no registrada
try:
    facu.inscribir_estudiante_en_materia("E01", "M99")
except MateriaNoEncontradaError as e:
    print("Error atrapado:", e)

# Inscripción correcta
facu.inscribir_estudiante_en_materia("E01", "M01")

# Prueba 3: Alumno ya inscripto
try:
    facu.inscribir_estudiante_en_materia("E01", "M01")
except EstudianteYaInscriptoError as e:
    print("Error atrapado:", e)

# Prueba 4: Cupo lleno
try:
    facu.inscribir_estudiante_en_materia("E02", "M01")
except CupoAgotadoError as e:
    print("Error atrapado:", e)