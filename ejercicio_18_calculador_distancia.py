# EJERCICIO 18 - Matriz de distancias
import math

class CalculadorDistancia:
    """Calcula distancias entre puntos 2D representados como tuplas."""

    def __init__(self):
        self.distancias = []   # historial de todas las distancias calculadas

    def distancia_euclidiana(self, p1, p2):
        """Distancia entre dos puntos (x, y)."""
        x1, y1 = p1               # desempaquetado de tupla
        x2, y2 = p2
        dx = x2 - x1
        dy = y2 - y1
        distancia = math.sqrt(dx ** 2 + dy ** 2)
        self.distancias.append(distancia)
        return distancia

    def punto_mas_cercano(self, referencia, *puntos):
        """Retorna el punto mas cercano a la referencia."""
        cercano = None
        minima = float("inf")     # infinito: cualquier distancia es menor
        for punto in puntos:
            d = self.distancia_euclidiana(referencia, punto)  
            if d < minima:
                minima = d
                cercano = punto
        return cercano


# Programa
if __name__ == "__main__":
    cd = CalculadorDistancia()

    print("distancia: ", cd.distancia_euclidiana((0, 0), (3, 4)))
    print("punto mas cercano: ", cd.punto_mas_cercano((0, 0), (3, 4), (1, 1), (6, 8)))
    print("Distancias calculadas: ", [round(d, 2) for d in cd.distancias])


# BOSQUEJO A MANO paso a paso
# distancia_euclidiana((0,0), (3,4))
#   p1 = (0,0) -> x1 = 0, y1 = 0     
#   p2 = (3,4) -> x2 = 3, y2 = 4
#   dx = 3 - 0 = 3     dy = 4 - 0 = 4
#   3**2 + 4**2 = 9 + 16 = 25
#   raiz de 25 = 5.0
#   distancias = [5.0]        <- se guarda en el atributo lista
#
# punto_mas_cercano((0,0), (3,4), (1,1), (6,8))
#   *puntos = ((3,4), (1,1), (6,8))
#   cercano = None   minima = infinito
#
#   (3,4) -> distancia 5.0       -> 5.0 < inf     ?   SI  -> cercano=(3,4), minima=5.0
#   (1,1) -> raiz(1+1) = 1.41    -> 1.41 < 5.0    ?   SI  -> cercano=(1,1), minima=1.41
#   (6,8) -> raiz(36+64) = 10.0  -> 10.0 < 1.41   ?   NO
#
#   return (1, 1)
#   distancias = [5.0, 5.0, 1.41, 10.0]   <- cada llamada agrega una
