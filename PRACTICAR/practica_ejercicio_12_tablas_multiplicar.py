# EJERCICIO 12 - Tablas de multiplicar con tuplas

class Tablas:
    """Crea tablas de multiplicar como tuplas."""

    def __init__(self):
        self.ultimo_resultado = []

    def crear_tabla(self, numero):
        """Retorna una TUPLA con la tabla del numero (del 1 al 5)."""
        resultado = []
        for i in range(1, 6):
            resultado.append(numero * i)
        return tuple(resultado)

    def tablas_combinadas(self, *numeros):
        """Junta varias tablas sin repetidos y ordenadas."""
        acumulado = set()
        for numero in numeros:
            for resultado in self.crear_tabla(numero):
                acumulado.add(resultado)
        self.ultimo_resultado = sorted(acumulado)
        return self.ultimo_resultado


# Programa
if __name__ == "__main__":
    t = Tablas()

    print("Tabla del 4: ", t.crear_tabla(4))
    print("Tablas del 2 y del 5: ", t.tablas_combinadas(2, 5))
