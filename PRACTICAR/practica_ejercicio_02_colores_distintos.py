# EJERCICIO 02 - Contador de colores distintos

class RegistroColores:
    """Guarda colores en una lista (con repetidos) y en un conjunto (sin repetidos)."""

    def __init__(self):
        self.lista = []
        self.distintos = set()

    def agregar_color(self, color):
        """Agrega el color a la lista y al conjunto."""
        self.lista.append(color)
        self.distintos.add(color)
        return color

    def agregar_varios(self, *args):
        """Agrega varios colores usando agregar_color."""
        for color in args:
            self.agregar_color(color)
        return self.lista

    def cantidad_distintos(self):
        """Retorna cuantos colores diferentes hay."""
        return len(self.distintos)


# Programa
if __name__ == "__main__":
    rc = RegistroColores()

    rc.agregar_varios("rojo", "verde", "rojo", "azul", "verde", "rojo")

    print("Lista: ", rc.lista)
    print("Conjunto: ", rc.distintos)
    print("Colores distintos: ", rc.cantidad_distintos())
