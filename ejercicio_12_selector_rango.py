# =============================================================================
# EJERCICIO 12 - Selector de rango con tuplas
# =============================================================================

class SelectorRango:
    """Genera rangos como tuplas y los combina sin duplicados."""

    def __init__(self):
        self.ultimo_resultado = []

    def crear_rango(self, inicio, fin):
        """Retorna una TUPLA con los numeros entre inicio y fin (inclusive)."""
        return tuple(range(inicio, fin + 1))   # +1 porque range excluye el fin

    def elementos_en_multiples_rangos(self, *rangos):
        """Combina varios rangos en una lista ordenada y sin duplicados."""
        acumulado = set()                      # el conjunto evita repetidos
        for rango in rangos:
            inicio, fin = rango                # desempaqueto la tupla
            numeros = self.crear_rango(inicio, fin)   # REUTILIZACION
            acumulado.update(numeros)          # union de conjuntos
        self.ultimo_resultado = sorted(acumulado)
        return self.ultimo_resultado


# --- Programa principal ---
if __name__ == "__main__":
    sr = SelectorRango()

    print("crear_rango(1, 3) ->", sr.crear_rango(1, 3))
    print("rangos (1,3)+(2,4)->", sr.elementos_en_multiples_rangos((1, 3), (2, 4)))


# =============================================================================
# BOSQUEJO A MANO - asi se ejecuta paso a paso
# =============================================================================
# crear_rango(1, 3)
#   range(1, 3 + 1) -> 1, 2, 3
#   return (1, 2, 3)      <- TUPLA
#
# elementos_en_multiples_rangos((1,3), (2,4))
#   *rangos = ((1,3), (2,4))     <- una tupla de tuplas
#   acumulado = set()            <- conjunto: elimina duplicados solo
#
#   rango (1,3) -> inicio=1, fin=3 -> crear_rango(1,3) = (1,2,3)
#                  acumulado = {1, 2, 3}
#
#   rango (2,4) -> inicio=2, fin=4 -> crear_rango(2,4) = (2,3,4)
#                  el 2 y el 3 YA estaban -> no se repiten
#                  acumulado = {1, 2, 3, 4}
#
#   sorted(acumulado) -> [1, 2, 3, 4]    <- el conjunto no tiene orden,
#                                           por eso hay que ordenarlo
