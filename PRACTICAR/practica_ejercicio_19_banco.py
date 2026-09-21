# EJERCICIO 19 - Cuentas de banco

class Banco:
    """Guarda el saldo de cada cliente en un diccionario: nombre -> saldo."""

    def __init__(self):
        self.cuentas = {}

    def depositar(self, nombre, monto):
        """Suma dinero a la cuenta del cliente."""
        if nombre in self.cuentas:
            self.cuentas[nombre] += monto
        else:
            self.cuentas[nombre] = monto
        return self.cuentas

    def retirar(self, nombre, monto):
        """Retira dinero. Retorna True si alcanzaba el saldo, si no False."""
        if nombre in self.cuentas and self.cuentas[nombre] >= monto:
            self.cuentas[nombre] -= monto
            return True
        return False

    def cuentas_saldo_bajo(self, minimo):
        """Retorna los clientes con saldo menor al minimo."""
        bajos = []
        for nombre, saldo in self.cuentas.items():
            if saldo < minimo:
                bajos.append(nombre)
        return bajos


# Programa
if __name__ == "__main__":
    b = Banco()

    b.depositar("Marta", 200)
    b.depositar("Pablo", 40)

    print("Retiro de Marta (50): ", b.retirar("Marta", 50))
    print("Retiro de Pablo (100): ", b.retirar("Pablo", 100))
    print("Cuentas: ", b.cuentas)
    print("Saldo menor a 100: ", b.cuentas_saldo_bajo(100))
