# EJERCICIO 11 - Contador de votos

class Votacion:
    """Cuenta los votos de cada candidato en un diccionario."""

    def __init__(self):
        self.votos = {}

    def votar(self, candidato):
        """Suma un voto al candidato."""
        if candidato in self.votos:
            self.votos[candidato] += 1
        else:
            self.votos[candidato] = 1
        return self.votos

    def votar_varios(self, *candidatos):
        """Suma varios votos usando votar."""
        for candidato in candidatos:
            self.votar(candidato)
        return self.votos

    def ganador(self):
        """Retorna el candidato con mas votos."""
        mejor = None
        maximo = 0
        for candidato, cantidad in self.votos.items():
            if cantidad > maximo:
                maximo = cantidad
                mejor = candidato
        return mejor

    def votos_de(self, candidato):
        """Retorna los votos del candidato (0 si no tiene)."""
        if candidato in self.votos:
            return self.votos[candidato]
        return 0


# Programa
if __name__ == "__main__":
    v = Votacion()

    v.votar_varios("Rosa", "Juan", "Rosa", "Juan", "Juan", "Mario")

    print("Votos: ", v.votos)
    print("Ganador: ", v.ganador())
    print("Votos de Rosa: ", v.votos_de("Rosa"))
    print("Votos de Pedro: ", v.votos_de("Pedro"))
