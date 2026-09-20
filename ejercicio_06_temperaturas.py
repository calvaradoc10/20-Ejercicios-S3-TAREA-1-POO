# EJERCICIO 06 - Estadisticas de temperatura
class GestorTemperatura:
    """Registra temperaturas en una lista y calcula estadisticas."""

    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        """Guarda una temperatura en la lista."""
        self.temperaturas.append(temp)
        return self.temperaturas

    def registrar_multiples(self, *temps):
        """Reutiliza registrar_temperatura para varias temperaturas."""
        for temp in temps:
            self.registrar_temperatura(temp)
        return self.temperaturas

    def minima(self):
        """Temperatura mas baja registrada."""
        if len(self.temperaturas) == 0:
            return None
        return min(self.temperaturas)

    def maxima(self):
        """Temperatura mas alta registrada."""
        if len(self.temperaturas) == 0:
            return None
        return max(self.temperaturas)

    def promedio(self):
        """Promedio de todas las temperaturas."""
        if len(self.temperaturas) == 0:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)


# Programa
if __name__ == "__main__":
    gt = GestorTemperatura()

    gt.registrar_multiples(20, 25, 18, 30)

    print("Temperaturas: ", gt.temperaturas)
    print("Minima: ", gt.minima())
    print("Maxima: ", gt.maxima())
    print("Promedio: ", gt.promedio())


# BOSQUEJO A MANO - asi se ejecuta paso a paso
# self.temperaturas = []
#
# registrar_multiples(20, 25, 18, 30)   
#   temp = 20 -> temperaturas = [20]
#   temp = 25 -> temperaturas = [20, 25]
#   temp = 18 -> temperaturas = [20, 25, 18]
#   temp = 30 -> temperaturas = [20, 25, 18, 30]
#
# minima()    -> min([20, 25, 18, 30]) = 18
# maxima()    -> max([20, 25, 18, 30]) = 30
# promedio()  -> suma = 20 + 25 + 18 + 30 = 93
#                93 / 4 = 23.25
