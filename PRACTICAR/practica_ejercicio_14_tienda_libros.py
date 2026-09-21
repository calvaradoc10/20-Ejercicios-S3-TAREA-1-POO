# EJERCICIO 14 - Tienda de libros

class TiendaLibros:
    """Guarda los libros en un diccionario: libro -> precio."""

    def __init__(self):
        self.libros = {}

    def registrar(self, libro, precio):
        """Guarda un libro con su precio."""
        self.libros[libro] = precio
        return self.libros

    def libros_menores_a(self, precio_maximo):
        """Retorna los libros que cuestan menos que precio_maximo."""
        lista = []
        for libro, precio in self.libros.items():
            if precio < precio_maximo:
                lista.append(libro)
        return lista

    def libro_mas_barato(self):
        """Retorna una TUPLA (libro, precio) del libro mas barato."""
        menor = min(self.libros.values())
        for libro, precio in self.libros.items():
            if precio == menor:
                return (libro, precio)


# Programa
if __name__ == "__main__":
    tl = TiendaLibros()

    tl.registrar("Harry Potter", 25)
    tl.registrar("Matilda", 10)
    tl.registrar("Dracula", 14)

    print("Libros: ", tl.libros)
    print("Menores a 15: ", tl.libros_menores_a(15))
    print("Mas barato: ", tl.libro_mas_barato())
