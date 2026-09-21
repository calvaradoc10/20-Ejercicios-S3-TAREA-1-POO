# EJERCICIO 05 - Clasificador de multiplos de 3

class ClasificadorNumeros:
    """Separa los numeros en multiplos de 3 y los demas."""

    def __init__(self):
        self.multiplos = []
        self.otros = []

    def es_multiplo_de_3(self, numero):
        """Retorna True si el numero es multiplo de 3."""
        return numero % 3 == 0

    def separar(self, *numeros):
        """Manda cada numero a su lista."""
        for n in numeros:
            if self.es_multiplo_de_3(n):
                self.multiplos.append(n)
            else:
                self.otros.append(n)
        return self.multiplos, self.otros

    def cantidades(self):
        """Retorna una tupla (cantidad de multiplos, cantidad de otros)."""
        return (len(self.multiplos), len(self.otros))


# Programa
if __name__ == "__main__":
    cn = ClasificadorNumeros()

    print("Separados: ", cn.separar(12, 5, 9, 20, 15, 8))
    print("Cantidades: ", cn.cantidades())
