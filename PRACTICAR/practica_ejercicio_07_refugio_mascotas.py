# EJERCICIO 07 - Refugio de mascotas

class RefugioMascotas:
    """Guarda las mascotas en un diccionario: nombre -> peso."""

    def __init__(self):
        self.mascotas = {}

    def agregar_mascota(self, nombre, peso):
        """Guarda una mascota con su peso."""
        self.mascotas[nombre] = peso
        return self.mascotas

    def mascotas_pesadas(self, peso_minimo):
        """Retorna los nombres de las mascotas que pesan peso_minimo o mas."""
        pesadas = []
        for nombre, peso in self.mascotas.items():
            if peso >= peso_minimo:
                pesadas.append(nombre)
        return pesadas

    def peso_promedio(self):
        """Retorna el promedio de los pesos."""
        return sum(self.mascotas.values()) / len(self.mascotas)


# Programa
if __name__ == "__main__":
    rm = RefugioMascotas()

    rm.agregar_mascota("Luna", 8)
    rm.agregar_mascota("Max", 25)
    rm.agregar_mascota("Nina", 5)
    rm.agregar_mascota("Bruno", 18)

    print("Mascotas: ", rm.mascotas)
    print("Pesan 10 o mas: ", rm.mascotas_pesadas(10))
    print("Peso promedio: ", rm.peso_promedio())
