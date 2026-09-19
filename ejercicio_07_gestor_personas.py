# =============================================================================
# EJERCICIO 07 - Mapeador de edades
# =============================================================================

class GestorPersonas:
    """Guarda personas en un diccionario nombre -> edad."""

    def __init__(self):
        self.personas = {}

    def agregar_persona(self, nombre, edad):
        """Guarda o actualiza la edad de una persona."""
        self.personas[nombre] = edad
        return self.personas

    def personas_mayores(self, edad_minima):
        """Retorna la lista de nombres con edad >= edad_minima."""
        mayores = []
        for nombre, edad in self.personas.items():
            if edad >= edad_minima:
                mayores.append(nombre)
        return mayores

    def edad_promedio(self):
        """Promedio de todas las edades guardadas."""
        if len(self.personas) == 0:
            return 0
        return sum(self.personas.values()) / len(self.personas)


# --- Programa principal ---
if __name__ == "__main__":
    gp = GestorPersonas()

    gp.agregar_persona("Ana", 28)
    gp.agregar_persona("Bob", 17)

    print("Personas          ->", gp.personas)
    print("Mayores de 18     ->", gp.personas_mayores(18))
    print("Edad promedio     ->", gp.edad_promedio())


# =============================================================================
# BOSQUEJO A MANO - asi se ejecuta paso a paso
# =============================================================================
# self.personas = {}       <- diccionario  nombre -> edad
#
# agregar_persona("Ana", 28) -> {"Ana": 28}
# agregar_persona("Bob", 17) -> {"Ana": 28, "Bob": 17}
#
# personas_mayores(18)
#   lista = []
#   recorro personas.items()  -> pares (clave, valor)
#
#   ("Ana", 28) -> 28 >= 18 ? SI -> lista = ["Ana"]
#   ("Bob", 17) -> 17 >= 18 ? NO -> no entra
#
#   return ["Ana"]
#
# edad_promedio()
#   (28 + 17) / 2 = 45 / 2 = 22.5
