# EJERCICIO 15 - Numeros primos

class Primos:
    """Busca numeros primos."""

    def __init__(self):
        self.resultados = {}   # limite -> cantidad de primos

    def es_primo(self, numero):
        """Retorna True si el numero es primo."""
        if numero < 2:
            return False
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True

    def primos_hasta(self, limite):
        """Retorna una TUPLA con los primos desde 2 hasta el limite."""
        primos = []
        for n in range(2, limite + 1):
            if self.es_primo(n):
                primos.append(n)
        return tuple(primos)

    def contar_primos(self, *limites):
        """Guarda en un diccionario cuantos primos hay hasta cada limite."""
        for limite in limites:
            self.resultados[limite] = len(self.primos_hasta(limite))
        return self.resultados


# Programa
if __name__ == "__main__":
    p = Primos()

    print("es_primo(13): ", p.es_primo(13))
    print("es_primo(15): ", p.es_primo(15))
    print("Primos hasta 30: ", p.primos_hasta(30))
    print("Cantidad de primos: ", p.contar_primos(5, 15, 25))
