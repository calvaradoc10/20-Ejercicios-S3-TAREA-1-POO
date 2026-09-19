# =============================================================================
# EJERCICIO 13 - Combinador de listas
# =============================================================================

class CombinadorListas:
    """Intercala listas elemento por elemento."""

    def __init__(self):
        self.ultimo_resultado = []

    def intercalar(self, lista1, lista2):
        """Alterna elementos de dos listas, aunque tengan distinto tamano."""
        resultado = []
        limite = max(len(lista1), len(lista2))
        for i in range(limite):
            if i < len(lista1):          # evita IndexError
                resultado.append(lista1[i])
            if i < len(lista2):
                resultado.append(lista2[i])
        return resultado

    def intercalar_multiples(self, *listas):
        """Intercala varias listas reutilizando intercalar()."""
        if len(listas) == 0:
            return []
        acumulado = list(listas[0])
        for lista in listas[1:]:
            acumulado = self.intercalar(acumulado, lista)   # REUTILIZACION
        self.ultimo_resultado = acumulado
        return acumulado


# --- Programa principal ---
if __name__ == "__main__":
    cl = CombinadorListas()

    print("intercalar([1,2],[3,4])  ->", cl.intercalar([1, 2], [3, 4]))
    print("intercalar_multiples     ->", cl.intercalar_multiples([1, 2], [3, 4], [5, 6]))
    print("listas de distinto largo ->", cl.intercalar([1, 2, 3, 4], [9]))


# =============================================================================
# BOSQUEJO A MANO - asi se ejecuta paso a paso
# =============================================================================
# intercalar([1,2], [3,4])
#   resultado = []
#   recorro i desde 0 hasta el largo de la lista mas larga (2)
#
#   i = 0 -> lista1 tiene indice 0 ? SI -> tomo 1 -> resultado = [1]
#            lista2 tiene indice 0 ? SI -> tomo 3 -> resultado = [1, 3]
#
#   i = 1 -> lista1[1] = 2 -> resultado = [1, 3, 2]
#            lista2[1] = 4 -> resultado = [1, 3, 2, 4]
#
#   return [1, 3, 2, 4]
#
# intercalar_multiples([1,2], [3,4], [5,6])   <- reutiliza el de arriba
#   acumulado = [1, 2]
#   con [3,4] -> intercalar([1,2], [3,4])     = [1, 3, 2, 4]
#   con [5,6] -> intercalar([1,3,2,4], [5,6]) = [1, 5, 3, 6, 2, 4]
