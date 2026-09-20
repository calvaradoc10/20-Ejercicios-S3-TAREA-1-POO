# EJERCICIO 11 - Contador de frecuencia
class ContadorFrecuencia:
    """Cuenta cuantas veces aparece cada elemento usando un diccionario."""

    def __init__(self):
        self.frecuencias = {}

    def agregar_elemento(self, elemento):
        """Suma 1 a la frecuencia del elemento (lo crea si no existe)."""
        if elemento in self.frecuencias:
            self.frecuencias[elemento] += 1
        else:
            self.frecuencias[elemento] = 1
        return self.frecuencias

    def agregar_multiples(self, *elementos):
        """Reutiliza agregar_elemento para varios elementos."""
        for elemento in elementos:
            self.agregar_elemento(elemento)
        return self.frecuencias

    def elemento_mas_frecuente(self):
        """Retorna el elemento que mas veces aparece."""
        mejor = None
        maximo = 0
        for elemento, veces in self.frecuencias.items():
            if veces > maximo:
                maximo = veces
                mejor = elemento
        return mejor

    def frecuencia_elemento(self, elemento):
        """Retorna cuantas veces aparece el elemento (0 si nunca aparecio)."""
        return self.frecuencias.get(elemento, 0)


# Programa
if __name__ == "__main__":
    cf = ContadorFrecuencia()

    cf.agregar_elemento("a")
    cf.agregar_elemento("b")
    cf.agregar_elemento("a")

    print("Frecuencias: ", cf.frecuencias)
    print("Mas frecuente: ", cf.elemento_mas_frecuente())
    print("frecuencia_elemento(b): ", cf.frecuencia_elemento("b"))
    print("frecuencia_elemento(z): ", cf.frecuencia_elemento("z"))


# BOSQUEJO A MANO paso a paso
# self.frecuencias = {}    diccionario  elemento -> cuantas veces
#
# agregar_elemento("a")
#   "a" no esta en el diccionario -> frecuencias["a"] = 1     ->  {"a": 1}
#
# agregar_elemento("b")
#   "b" no esta -> frecuencias["b"] = 1                       ->  {"a":1, "b":1}
#
# agregar_elemento("a")
#   "a" si esta -> frecuencias["a"] = 1 + 1 = 2               ->  {"a":2, "b":1}
#
# elemento_mas_frecuente()
#   mejor = None   maximo = 0
#   ("a", 2)  2 > 0   ?    SI   -> mejor = "a", maximo = 2
#   ("b", 1)  1 > 2   ?    NO   -> no cambia
#   return "a"
#
# frecuencia_elemento("b") -> 1
# frecuencia_elemento("z") -> no existe con .get("z", 0) retorna 0
