# EJERCICIO 13 - Unir listas sin repetir

class UnidorListas:
    """Une listas sin dejar elementos repetidos."""

    def __init__(self):
        self.ultimo_resultado = []

    def unir_sin_repetir(self, lista1, lista2):
        """Retorna una lista con los elementos de las dos listas, sin repetir."""
        resultado = []
        for elemento in lista1:
            if elemento not in resultado:
                resultado.append(elemento)
        for elemento in lista2:
            if elemento not in resultado:
                resultado.append(elemento)
        return resultado

    def unir_varias(self, *listas):
        """Une varias listas usando unir_sin_repetir."""
        acumulado = []
        for lista in listas:
            acumulado = self.unir_sin_repetir(acumulado, lista)
        self.ultimo_resultado = acumulado
        return acumulado


# Programa
if __name__ == "__main__":
    ul = UnidorListas()

    print("Unir dos listas: ", ul.unir_sin_repetir([5, 6, 7], [7, 8, 5]))
    print("Unir varias: ", ul.unir_varias([9, 8], [8, 7], [7, 6, 9]))
