# EJERCICIO 16 - Codificador de vocales

class CodificadorVocales:
    """Cambia cada vocal por un numero (a=1, e=2, i=3, o=4, u=5)."""

    def __init__(self):
        self.codigo = {"a": "1", "e": "2", "i": "3", "o": "4", "u": "5"}
        self.inverso = {"1": "a", "2": "e", "3": "i", "4": "o", "5": "u"}
        self.historial = {}   # palabra original -> palabra codificada

    def codificar_letra(self, letra):
        """Si es vocal la cambia por su numero, si no la deja igual."""
        if letra in self.codigo:
            return self.codigo[letra]
        return letra

    def decodificar_letra(self, simbolo):
        """Si es un numero del codigo lo cambia por su vocal."""
        if simbolo in self.inverso:
            return self.inverso[simbolo]
        return simbolo

    def codificar_palabra(self, palabra):
        """Codifica la palabra usando codificar_letra."""
        resultado = ""
        for letra in palabra:
            resultado = resultado + self.codificar_letra(letra)
        self.historial[palabra] = resultado
        return resultado

    def decodificar_palabra(self, palabra):
        """Decodifica la palabra usando decodificar_letra."""
        resultado = ""
        for simbolo in palabra:
            resultado = resultado + self.decodificar_letra(simbolo)
        return resultado


# Programa
if __name__ == "__main__":
    cv = CodificadorVocales()

    print("Letra codificada: ", cv.codificar_letra("e"))
    print("Palabra codificada: ", cv.codificar_palabra("programacion"))
    print("Palabra decodificada: ", cv.decodificar_palabra("h4l1"))
    print("Historial: ", cv.historial)
