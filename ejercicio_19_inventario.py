# EJERCICIO 19 - Inventario de productos
class Inventario:
    """Inventario simple basado en un diccionario producto -> cantidad."""

    def __init__(self):
        self.stock = {}

    def agregar_stock(self, producto, cantidad):
        """Suma cantidad al producto (lo crea si no existe)."""
        if producto in self.stock:
            self.stock[producto] += cantidad
        else:
            self.stock[producto] = cantidad
        return self.stock

    def restar_stock(self, producto, cantidad):
        """Descuenta stock. Retorna True solo si habia suficiente."""
        if producto not in self.stock:
            return False
        if self.stock[producto] >= cantidad:
            self.stock[producto] -= cantidad
            return True
        return False                 # no alcanza: no se toca el diccionario

    def productos_bajo_stock(self, minimo):
        """Retorna los productos con cantidad menor que el minimo."""
        bajos = []
        for producto, cantidad in self.stock.items():
            if cantidad < minimo:
                bajos.append(producto)
        return bajos


# Programa
if __name__ == "__main__":
    inv = Inventario()

    inv.agregar_stock("pan", 50)
    print("Resta de stock: ", inv.restar_stock("pan", 30))
    print("Stock actual: ", inv.stock)
    print("Bajo stock: ", inv.productos_bajo_stock(15))
    print("Bajo stock: ", inv.productos_bajo_stock(25))
    print("Resta de stock: ", inv.restar_stock("pan", 999))


# BOSQUEJO A MANO  paso a paso
# self.stock = {}           diccionario  producto -> cantidad
#
# agregar_stock("pan", 50)
#   "pan" no existe -> stock["pan"] = 50      -> {"pan": 50}
#
# restar_stock("pan", 30)
#   existe "pan"     ? SI
#   50 >= 30         ? SI  -> stock["pan"] = 50 - 30 = 20
#   return True                                -> {"pan": 20}
#
# productos_bajo_stock(15)
#   ("pan", 20)   20 < 15   ?   NO   -> no entra
#   return []     <-- vacia
#
# Con minimo = 25 si aparece:
#   ("pan", 20)   20 < 25  ?    SI   -> ["pan"]
