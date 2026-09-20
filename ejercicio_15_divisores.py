# EJERCICIO 15 - Divisores de un numero
class DivisorFinder:
    """Encuentra divisores y detecta numeros perfectos."""

    def __init__(self):
        self.historial = {}   # numero -> tupla de divisores

    def encontrar_divisores(self, numero):
        """Retorna una TUPLA con todos los divisores del numero."""
        divisores = []
        for i in range(1, numero + 1):
            if numero % i == 0:          # division exacta
                divisores.append(i)
        return tuple(divisores)          # lista -> tupla 

    def es_perfecto(self, numero):
        """True si la suma de los divisores propios es igual al numero."""
        divisores = self.encontrar_divisores(numero)   
        propios = divisores[:-1]                       # todos menos el mismo
        return sum(propios) == numero

    def encontrar_multiples_divisores(self, *numeros):
        """Retorna un diccionario {numero: tupla_divisores}."""
        for numero in numeros:
            self.historial[numero] = self.encontrar_divisores(numero)
        return self.historial


# Programa 
if __name__ == "__main__":
    df = DivisorFinder()

    print("encontrar_divisores: ", df.encontrar_divisores(12))
    print("es_perfecto: ", df.es_perfecto(6))
    print("es_perfecto: ", df.es_perfecto(12))
    print("multiples divisores: ", df.encontrar_multiples_divisores(6, 12))


# BOSQUEJO A MANO - asi se ejecuta paso a paso
# encontrar_divisores(12)
#   divisores = []
#   pruebo i de 1 hasta 12
#
#   i =   1 -> 12 % 1 = 0 ->   SI  -> [1]
#   i =   2 -> 12 % 2 = 0 ->   SI  -> [1, 2]
#   i =   3 -> 12 % 3 = 0 ->   SI  -> [1, 2, 3]
#   i =   4 -> 12 % 4 = 0 ->   SI  -> [1, 2, 3, 4]
#   i =   5 -> 12 % 5 = 2 ->   NO
#   i =   6 -> 12 % 6 = 0 ->   SI  -> [1, 2, 3, 4, 6]
#   i =   7..11 -> ninguno divide exacto
#   i = 12 -> 12 % 12 = 0 ->   SI  -> [1, 2, 3, 4, 6, 12]
#
#   return (1, 2, 3, 4, 6, 12)    <- convertido a TUPLA
#
# es_perfecto(6)
#   divisores de 6 = (1, 2, 3, 6)
#   quito el propio numero -> 1 + 2 + 3 = 6
#   6 == 6 -> True
#
# es_perfecto(12)
#   divisores = (1,2,3,4,6,12) -> 1+2+3+4+6 = 16
#   16 == 12 ?     NO   -> False
