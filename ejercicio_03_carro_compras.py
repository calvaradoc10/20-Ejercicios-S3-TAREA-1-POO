# EJERCICIO 03 - Gestor de compras con totales
class CarroCompras:
    """Carro de compras basado en un diccionario nombre: precio."""

    def __init__(self):
        self.carrito = {}   # diccionario vacio

    def agregar_articulo(self, nombre, precio):
        """Guarda o actualiza el precio de un articulo."""
        self.carrito[nombre] = precio
        return self.carrito

    def total_carrito(self):
        """Suma todos los precios guardados."""
        total = 0
        for precio in self.carrito.values():   # .values() = solo los precios
            total = total + precio
        return total

    def articulos_por_rango(self, precio_min, precio_max):
        """Retorna la lista de articulos cuyo precio esta dentro del rango."""
        encontrados = []
        for nombre, precio in self.carrito.items():   # .items() = clave y valor, .keys() solo es clave
            if precio_min <= precio <= precio_max:
                encontrados.append(nombre)
        return encontrados


# Programa
if __name__ == "__main__":
    c = CarroCompras()

    c.agregar_articulo("pan", 2.50)
    c.agregar_articulo("leche", 3.00)

    print("Carrito: ", c.carrito)
    print("Total: ", c.total_carrito())
    print("Entre 2.00 y 2.90: ", c.articulos_por_rango(2.00, 2.90))


# BOSQUEJO A MANO paso a paso
# self.carrito = {}        <- diccionario  nombre -> precio
#
# agregar_articulo("pan", 2.50)
#   carrito["pan"] = 2.50    -> {"pan": 2.5}
#
# agregar_articulo("leche", 3.00)
#   carrito["leche"] = 3.00  -> {"pan": 2.5, "leche": 3.0}
#
# total_carrito()
#   total = 0
#   recorro carrito.values()
#     precio = 2.5  -> total = 0   + 2.5 = 2.5
#     precio = 3.0  -> total = 2.5 + 3.0 = 5.5
#   return 5.5
#
# articulos_por_rango(2.00, 2.90)
#   ("pan", 2.5)   -> 2.00 <= 2.5 <= 2.90 ? SI -> ["pan"]
#   ("leche", 3.0) -> 3.0 <= 2.90 ? NO         -> se descarta
#   return ["pan"]
