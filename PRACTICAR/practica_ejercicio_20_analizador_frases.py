# EJERCICIO 20 - Analizador de frases

class AnalizadorFrases:
    """Analiza las palabras de una frase."""

    def __init__(self):
        self.palabras = []

    def palabras_que_terminan_con(self, texto, final):
        """Retorna las palabras del texto que terminan con 'final'."""
        encontradas = []
        for palabra in texto.split():
            if palabra.endswith(final):
                encontradas.append(palabra)
        return encontradas

    def agrupar_por_inicial(self, texto):
        """Agrupa las palabras segun su primera letra."""
        grupos = {}
        for palabra in texto.split():
            self.palabras.append(palabra)
            inicial = palabra[0]
            if inicial not in grupos:
                grupos[inicial] = []
            grupos[inicial].append(palabra)
        return grupos

    def palabras_distintas(self):
        """Retorna el CONJUNTO de palabras distintas analizadas."""
        return set(self.palabras)


# Programa
if __name__ == "__main__":
    af = AnalizadorFrases()

    texto = "mi perro come pan y mi gato come pescado"

    print("Agrupado por inicial: ", af.agrupar_por_inicial(texto))
    print("Terminan con 'o': ", af.palabras_que_terminan_con(texto, "o"))
    print("Palabras distintas: ", af.palabras_distintas())
    print("Cuantas distintas: ", len(af.palabras_distintas()))
