# EJERCICIO 06 - Registro de gastos

class RegistroGastos:
    """Guarda gastos en una lista."""

    def __init__(self):
        self.gastos = []

    def registrar_gasto(self, monto):
        """Guarda un gasto."""
        self.gastos.append(monto)
        return self.gastos

    def registrar_varios(self, *montos):
        """Guarda varios gastos usando registrar_gasto."""
        for monto in montos:
            self.registrar_gasto(monto)
        return self.gastos

    def gasto_mayor(self):
        """Retorna el gasto mas alto."""
        return max(self.gastos)

    def gasto_menor(self):
        """Retorna el gasto mas bajo."""
        return min(self.gastos)

    def total_gastado(self):
        """Retorna la suma de todos los gastos."""
        return sum(self.gastos)


# Programa
if __name__ == "__main__":
    rg = RegistroGastos()

    rg.registrar_varios(50, 12, 30, 7, 21)

    print("Gastos: ", rg.gastos)
    print("Mayor: ", rg.gasto_mayor())
    print("Menor: ", rg.gasto_menor())
    print("Total: ", rg.total_gastado())
