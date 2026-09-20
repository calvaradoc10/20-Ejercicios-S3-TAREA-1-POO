# EJERCICIO 08 - Asignador de equipos
class Equipos:
    """Diccionario de listas: cada equipo guarda su lista de jugadores."""

    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        """Crea un equipo nuevo con una lista vacia de jugadores."""
        if nombre_equipo not in self.equipos:
            self.equipos[nombre_equipo] = []
        return self.equipos

    def agregar_jugador(self, equipo, jugador):
        """Agrega un jugador a la lista del equipo indicado."""
        if equipo not in self.equipos:      # si no existe, lo creo
            self.crear_equipo(equipo)
        self.equipos[equipo].append(jugador)
        return self.equipos[equipo]

    def equipo_mayor_integrantes(self):
        """Retorna el nombre del equipo con mas jugadores."""
        mayor = ""
        maximo = 0
        for nombre, jugadores in self.equipos.items():
            if len(jugadores) > maximo:
                maximo = len(jugadores)
                mayor = nombre
        return mayor


# Programa principal
if __name__ == "__main__":
    eq = Equipos()

    eq.crear_equipo("A")
    eq.agregar_jugador("A", "Juan")
    eq.agregar_jugador("A", "Pedro")
    eq.crear_equipo("B")
    eq.agregar_jugador("B", "Luis")

    print("Equipos: ", eq.equipos)
    print("Equipo con mas jugadores: ", eq.equipo_mayor_integrantes())

# BOSQUEJO A MANO paso a paso
# self.equipos = {}        diccionario  equipo -> LISTA de jugadores
#
# crear_equipo("A")             -> {"A": []}
# agregar_jugador("A", "Juan")  -> {"A": ["Juan"]}
# agregar_jugador("A", "Pedro") -> {"A": ["Juan", "Pedro"]}
# crear_equipo("B")             -> {"A": ["Juan","Pedro"], "B": []}
# agregar_jugador("B", "Luis")  -> {"A": ["Juan","Pedro"], "B": ["Luis"]}
#
# equipo_mayor_integrantes()
#   mayor = ""   maximo = 0
#
#   "A" len(["Juan","Pedro"]) = 2  ->  2 > 0 ?   SI -> mayor = "A", maximo = 2
#   "B" len(["Luis"])         = 1  ->  1 > 2 ?   NO -> no cambia
#
#   return "A"
