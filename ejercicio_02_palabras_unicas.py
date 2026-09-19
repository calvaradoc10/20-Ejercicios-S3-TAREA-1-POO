# =============================================================================
# EJERCICIO 02 - Contador de palabras unicas
# =============================================================================

class AnalizadorTexto:
    """Guarda palabras en un conjunto (unicas) y en una lista (orden)."""

    def __init__(self):
        self.unicas = set()   # conjunto: elimina duplicados automaticamente
        self.orden = []       # lista: conserva el orden de llegada

    def agregar_palabra(self, palabra):
        """Agrega una palabra al conjunto y a la lista."""
        palabra = palabra.lower()     # normaliza: Hola == hola
        self.unicas.add(palabra)      # add() es de conjuntos
        self.orden.append(palabra)    # append() es de listas
        return palabra

    def agregar_multiples(self, *args):
        """Reutiliza agregar_palabra para varias palabras a la vez."""
        for palabra in args:
            self.agregar_palabra(palabra)
        return self.orden

    def contar_palabras(self):
        """Retorna cuantas palabras DISTINTAS se han agregado."""
        return len(self.unicas)


# --- Programa principal ---
if __name__ == "__main__":
    at = AnalizadorTexto()

    at.agregar_multiples("hola", "mundo", "hola")

    print("Lista con orden   ->", at.orden)
    print("Conjunto de unicas->", at.unicas)
    print("Palabras unicas   ->", at.contar_palabras())


# =============================================================================
# BOSQUEJO A MANO - asi se ejecuta paso a paso
# =============================================================================
# self.unicas = set()      <- conjunto: NO admite repetidos
# self.orden  = []         <- lista   : SI admite repetidos
#
# agregar_multiples("hola", "mundo", "hola")
#   *args = ("hola", "mundo", "hola")
#
#   vuelta 1 -> palabra = "hola"
#       unicas.add("hola")   -> {"hola"}
#       orden.append("hola") -> ["hola"]
#
#   vuelta 2 -> palabra = "mundo"
#       unicas.add("mundo")  -> {"hola", "mundo"}
#       orden.append(...)    -> ["hola", "mundo"]
#
#   vuelta 3 -> palabra = "hola"   <-- REPETIDA
#       unicas.add("hola")   -> {"hola", "mundo"}  (el conjunto la ignora,
#                                                   NO da error)
#       orden.append("hola") -> ["hola", "mundo", "hola"]
#
# contar_palabras()
#   len(unicas) = 2
