# EJERCICIO 08 - Cursos con sus alumnos

class Cursos:
    """Diccionario donde cada curso tiene una lista de alumnos."""

    def __init__(self):
        self.cursos = {}

    def crear_curso(self, nombre):
        """Crea un curso con una lista vacia."""
        if nombre not in self.cursos:
            self.cursos[nombre] = []
        return self.cursos

    def agregar_alumno(self, curso, alumno):
        """Agrega un alumno a la lista del curso."""
        if curso not in self.cursos:
            self.crear_curso(curso)
        self.cursos[curso].append(alumno)
        return self.cursos[curso]

    def curso_mas_grande(self):
        """Retorna el nombre del curso con mas alumnos."""
        mayor = ""
        maximo = 0
        for nombre, alumnos in self.cursos.items():
            if len(alumnos) > maximo:
                maximo = len(alumnos)
                mayor = nombre
        return mayor


# Programa
if __name__ == "__main__":
    c = Cursos()

    c.crear_curso("Historia")
    c.agregar_alumno("Historia", "Carla")
    c.agregar_alumno("Historia", "Diego")
    c.agregar_alumno("Arte", "Elena")
    c.agregar_alumno("Historia", "Marta")

    print("Cursos: ", c.cursos)
    print("Curso mas grande: ", c.curso_mas_grande())
