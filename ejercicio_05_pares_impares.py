# EJERCICIO 05 - Detector de numeros pares e impares
class AnalizadorNumeros:
    """Clasifica numeros en pares e impares usando el operador modulo."""

    def __init__(self):
        self.clasificacion = {"pares": [], "impares": []}

    def es_par(self, numero):
        """Retorna True si el numero es par."""
        return numero % 2 == 0

    def separar(self, *numeros):
        """Clasifica todos los numeros recibidos en pares e impares."""
        for n in numeros:
            if self.es_par(n):                        # REUTILIZACION
                self.clasificacion["pares"].append(n)
            else:
                self.clasificacion["impares"].append(n)
        return self.clasificacion

    def cantidad_pares_impares(self):
        """Retorna una TUPLA (cantidad de pares, cantidad de impares)."""
        return (len(self.clasificacion["pares"]),
                len(self.clasificacion["impares"]))


# Programa principal 
if __name__ == "__main__":
    an = AnalizadorNumeros()

    print("Separa: ", an.separar(1, 2, 3, 4, 5))
    print("Cantidad de pares e impares", an.cantidad_pares_impares())


# BOSQUEJO A MANO paso a paso
# separar(1, 2, 3, 4, 5)
#   resultado = {"pares": [], "impares": []}  
#   *numeros = (1, 2, 3, 4, 5)
#
#   es_par():
#   n = 1 -> 1 % 2 = 1 ->  False  -> impares = [1]
#   n = 2 -> 2 % 2 = 0 ->  True   -> pares   = [2]
#   n = 3 -> 3 % 2 = 1 ->  False  -> impares = [1, 3]
#   n = 4 -> 4 % 2 = 0 ->  True   -> pares   = [2, 4]
#   n = 5 -> 5 % 2 = 1 ->  False  -> impares = [1, 3, 5]
#
#   return {"pares": [2, 4], "impares": [1, 3, 5]}
#
# cantidad_pares_impares()
#   len(pares) = 2 ; len(impares) = 3
#   return (2, 3)
