# EJERCICIO 03 - Menu de restaurante

class Menu:
    """Guarda los platos en un diccionario: nombre -> precio."""

    def __init__(self):
        self.platos = {}

    def agregar_plato(self, nombre, precio):
        """Guarda un plato con su precio."""
        self.platos[nombre] = precio
        return self.platos

    def precio_total(self):
        """Suma los precios de todos los platos."""
        total = 0
        for precio in self.platos.values():
            total = total + precio
        return total

    def platos_baratos(self, limite):
        """Retorna los platos que cuestan el limite o menos."""
        baratos = []
        for nombre, precio in self.platos.items():
            if precio <= limite:
                baratos.append(nombre)
        return baratos


# Programa
if __name__ == "__main__":
    m = Menu()

    m.agregar_plato("pollo", 6.50)
    m.agregar_plato("arroz", 1.50)
    m.agregar_plato("cola", 1.00)
    m.agregar_plato("flan", 2.50)

    print("Menu: ", m.platos)
    print("Total: ", m.precio_total())
    print("Platos hasta 3 dolares: ", m.platos_baratos(3))
