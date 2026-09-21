# EJERCICIO 18 - Distancias entre puntos

class Mapa:
    """Calcula distancias entre puntos (x, y) guardados como tuplas."""

    def __init__(self):
        self.distancias = []   # guarda cada distancia calculada

    def distancia(self, p1, p2):
        """Distancia por cuadras: |x2 - x1| + |y2 - y1|."""
        x1, y1 = p1
        x2, y2 = p2
        d = abs(x2 - x1) + abs(y2 - y1)
        self.distancias.append(d)
        return d

    def punto_mas_cercano(self, referencia, *puntos):
        """Retorna el punto que esta mas cerca de la referencia."""
        cercano = None
        minima = 9999      # un numero muy grande para empezar
        for punto in puntos:
            d = self.distancia(referencia, punto)
            if d < minima:
                minima = d
                cercano = punto
        return cercano


# Programa
if __name__ == "__main__":
    m = Mapa()

    print("Distancia: ", m.distancia((1, 1), (5, 2)))
    print("Punto mas cercano: ", m.punto_mas_cercano((0, 0), (4, 4), (2, 1), (5, 0)))
    print("Historial: ", m.distancias)
