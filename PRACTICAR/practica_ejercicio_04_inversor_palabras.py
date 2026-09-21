# EJERCICIO 04 - Inversor de palabras

class InversorPalabras:
    """Invierte palabras recorriendolas de atras hacia adelante."""

    def __init__(self):
        self.historial = {}   # palabra -> palabra invertida

    def invertir_palabra(self, palabra):
        """Retorna la palabra al reves."""
        resultado = ""
        # recorro los indices desde el ultimo hasta el 0
        for i in range(len(palabra) - 1, -1, -1):
            resultado = resultado + palabra[i]
        return resultado

    def invertir_varias(self, *palabras):
        """Invierte varias palabras y las guarda en el diccionario."""
        for palabra in palabras:
            self.historial[palabra] = self.invertir_palabra(palabra)
        return self.historial


# Programa
if __name__ == "__main__":
    ip = InversorPalabras()

    print("Invertida: ", ip.invertir_palabra("gato"))
    print("Varias: ", ip.invertir_varias("sol", "luna", "computador"))
