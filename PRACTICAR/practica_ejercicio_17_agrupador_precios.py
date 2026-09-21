# EJERCICIO 17 - Agrupador de precios por categoria

class AgrupadorPrecios:
    """Clasifica precios en barato, medio o caro."""

    def __init__(self):
        self.grupos = {}

    def clasificar_precio(self, precio):
        """Retorna la categoria del precio."""
        if precio < 10:
            return "barato"
        elif precio < 50:
            return "medio"
        else:
            return "caro"

    def agrupar(self, *precios):
        """Agrupa los precios en un diccionario de listas."""
        for precio in precios:
            categoria = self.clasificar_precio(precio)
            if categoria not in self.grupos:
                self.grupos[categoria] = []
            self.grupos[categoria].append(precio)
        return self.grupos

    def promedio_categoria(self, categoria):
        """Retorna el promedio de los precios de una categoria."""
        if categoria not in self.grupos:
            return 0
        lista = self.grupos[categoria]
        return sum(lista) / len(lista)


# Programa
if __name__ == "__main__":
    ap = AgrupadorPrecios()

    print("Categoria de 60: ", ap.clasificar_precio(60))
    print("Agrupado: ", ap.agrupar(4, 9, 15, 45, 55, 200))
    print("Promedio de caro: ", ap.promedio_categoria("caro"))
