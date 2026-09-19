# =============================================================================
# EJERCICIO 16 - Codificador / Decodificador Cesar
# =============================================================================

class CodificadorCesar:
    """Cifrado Cesar: desplaza cada letra N posiciones en el alfabeto."""

    def __init__(self):
        self.historial = {}   # diccionario  original -> codificada

    def codificar_letra(self, letra, desplazamiento):
        """Desplaza una sola letra usando el operador modulo."""
        if not letra.isalpha():            # espacios y signos no se tocan
            return letra

        if letra.isupper():
            base = ord("A")
        else:
            base = ord("a")

        posicion = ord(letra) - base                   # 0 a 25
        nueva = (posicion + desplazamiento) % 26       # el % da la vuelta
        return chr(nueva + base)

    def codificar_palabra(self, palabra, desplazamiento):
        """Codifica la palabra completa reutilizando codificar_letra."""
        codificada = ""
        for letra in palabra:
            codificada += self.codificar_letra(letra, desplazamiento)
        self.historial[palabra] = codificada
        return codificada

    def decodificar_palabra(self, palabra, desplazamiento):
        """Decodifica usando el desplazamiento contrario."""
        return self.codificar_palabra(palabra, -desplazamiento)


# --- Programa principal ---
if __name__ == "__main__":
    cc = CodificadorCesar()

    print("codificar_letra('h', 3)     ->", cc.codificar_letra("h", 3))
    print("codificar_letra('z', 3)     ->", cc.codificar_letra("z", 3))
    print("codificar_palabra('hola',3) ->", cc.codificar_palabra("hola", 3))
    print("decodificar 'krod'          ->", cc.decodificar_palabra("krod", 3))
    print("Historial                   ->", cc.historial)


# =============================================================================
# BOSQUEJO A MANO - asi se ejecuta paso a paso
# =============================================================================
# codificar_letra(letra, 3) usa: (posicion + desplazamiento) % 26
#
# 'h' -> ord('h') = 104 -> 104-97 = 7  -> (7+3)  % 26 = 10 -> 10+97 = 107 -> 'k'
# 'o' -> ord('o') = 111 -> 111-97 = 14 -> (14+3) % 26 = 17 -> 'r'
# 'l' -> ord('l') = 108 -> 108-97 = 11 -> (11+3) % 26 = 14 -> 'o'
# 'a' -> ord('a') = 97  -> 97-97  = 0  -> (0+3)  % 26 = 3  -> 'd'
#
# codificada = "krod"
# historial = {"hola": "krod"}
#
# Por que el % 26: prueba con la 'z'
#   'z' -> 122 - 97 = 25 -> (25 + 3) % 26 = 28 % 26 = 2 -> 'c'
#   o sea, al pasarse del final vuelve al principio del abecedario.
