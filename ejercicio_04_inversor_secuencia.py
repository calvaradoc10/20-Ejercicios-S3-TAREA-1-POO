# =============================================================================
# EJERCICIO 04 - Inversor de secuencias
# =============================================================================

class InversorSecuencia:
    """Invierte listas manualmente, sin reversed() ni [::-1]."""

    def __init__(self):
        self.invertidas = {}   # historial de inversiones

    def invertir_lista(self, lista):
        """Retorna una lista nueva con los elementos al reves."""
        resultado = []
        # range(ultimo_indice, -1, -1) recorre hacia atras: 2, 1, 0
        for i in range(len(lista) - 1, -1, -1):
            resultado.append(lista[i])
        return resultado

    def invertir_multiples(self, *listas):
        """Invierte varias listas y las guarda en un diccionario."""
        for lista in listas:
            clave = tuple(lista)                    # la clave debe ser inmutable
            self.invertidas[clave] = self.invertir_lista(lista)
        return self.invertidas


# --- Programa principal ---
if __name__ == "__main__":
    inv = InversorSecuencia()

    print("invertir_lista([1,2,3]) ->", inv.invertir_lista([1, 2, 3]))
    print("invertir_multiples      ->", inv.invertir_multiples([1, 2], [3, 4]))


# =============================================================================
# BOSQUEJO A MANO - asi se ejecuta paso a paso
# =============================================================================
# invertir_lista([1, 2, 3])
#   resultado = []
#   recorro los indices hacia atras: range(2, -1, -1) -> 2, 1, 0
#
#   i = 2 -> lista[2] = 3 -> resultado = [3]
#   i = 1 -> lista[1] = 2 -> resultado = [3, 2]
#   i = 0 -> lista[0] = 1 -> resultado = [3, 2, 1]
#   return [3, 2, 1]
#
# invertir_multiples([1,2], [3,4])
#   *listas = ([1,2], [3,4])
#   diccionario = {}
#
#   lista [1,2] -> la clave NO puede ser una lista (no es hashable)
#                  clave = tuple([1,2]) = (1, 2)
#                  valor = invertir_lista([1,2]) = [2, 1]
#                  -> {(1,2): [2,1]}
#
#   lista [3,4] -> clave = (3, 4)
#                  valor = [4, 3]
#                  -> {(1,2): [2,1], (3,4): [4,3]}
