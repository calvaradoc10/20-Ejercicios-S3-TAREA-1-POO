# =============================================================================
# EJERCICIO 14 - Mapeo de estudiantes a notas
# =============================================================================

class RegistroNotas:
    """Registro de notas por estudiante usando un diccionario."""

    def __init__(self):
        self.notas = {}

    def registrar(self, estudiante, nota):
        """Guarda o actualiza la nota de un estudiante."""
        self.notas[estudiante] = nota
        return self.notas

    def estudiantes_aprobados(self, nota_minima):
        """Retorna la lista de estudiantes con nota >= nota_minima."""
        aprobados = []
        for estudiante, nota in self.notas.items():
            if nota >= nota_minima:
                aprobados.append(estudiante)
        return aprobados

    def mejor_estudiante(self):
        """Retorna una TUPLA (nombre, nota) del mejor estudiante."""
        mejor = None
        mayor = -1
        for estudiante, nota in self.notas.items():
            if nota > mayor:
                mayor = nota
                mejor = estudiante
        return (mejor, mayor)


# --- Programa principal ---
if __name__ == "__main__":
    rn = RegistroNotas()

    rn.registrar("Ana", 95)
    rn.registrar("Bob", 70)

    print("Registro            ->", rn.notas)
    print("Aprobados (80)      ->", rn.estudiantes_aprobados(80))
    print("Mejor estudiante    ->", rn.mejor_estudiante())


# =============================================================================
# BOSQUEJO A MANO - asi se ejecuta paso a paso
# =============================================================================
# self.notas = {}          <- diccionario  estudiante -> nota
#
# registrar("Ana", 95) -> {"Ana": 95}
# registrar("Bob", 70) -> {"Ana": 95, "Bob": 70}
#
# estudiantes_aprobados(80)
#   ("Ana", 95) -> 95 >= 80 ? SI -> ["Ana"]
#   ("Bob", 70) -> 70 >= 80 ? NO
#   return ["Ana"]
#
# mejor_estudiante()
#   mejor = None   mayor = -1
#   ("Ana", 95) -> 95 > -1 ? SI -> mejor = "Ana", mayor = 95
#   ("Bob", 70) -> 70 > 95 ? NO -> no cambia
#   return ("Ana", 95)       <- TUPLA (nombre, nota)
