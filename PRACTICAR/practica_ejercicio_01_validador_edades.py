# EJERCICIO 01 - Validador de edades con promedio

class RegistroEdades:
    """Guarda solo las edades validas (entre 0 y 120) y saca el promedio."""

    def __init__(self):
        self.edades = []

    def es_valida(self, edad):
        """Retorna True si la edad esta entre 0 y 120."""
        return 0 <= edad <= 120

    def cargar_edades(self, *args):
        """Recibe varias edades y guarda solo las validas."""
        for edad in args:
            if self.es_valida(edad):
                self.edades.append(edad)
        return self.edades

    def promedio(self):
        """Retorna el promedio de las edades guardadas."""
        return sum(self.edades) / len(self.edades)


# Programa
if __name__ == "__main__":
    r = RegistroEdades()

    print("es_valida(60): ", r.es_valida(60))
    print("es_valida(-5): ", r.es_valida(-5))
    print("Edades validas: ", r.cargar_edades(12, 45, 200, 60, -1, 30))
    print("Promedio: ", r.promedio())
