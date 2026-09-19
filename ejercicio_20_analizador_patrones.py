# =============================================================================
# EJERCICIO 20 - Analizador de patrones en textos
# =============================================================================

class AnalizadorPatrones:
    """Analiza textos: filtra por patron, agrupa por longitud y saca unicas."""

    def __init__(self):
        self.palabras = []   # todas las palabras analizadas

    def encontrar_palabras(self, texto, patron):
        """Retorna las palabras del texto que empiezan con el patron."""
        encontradas = []
        for palabra in texto.split():
            if palabra.lower().startswith(patron.lower()):
                encontradas.append(palabra)
        return encontradas

    def agrupar_por_longitud(self, texto):
        """Agrupa las palabras del texto segun su cantidad de letras."""
        grupos = {}
        for palabra in texto.split():
            self.palabras.append(palabra)     # se guardan para palabras_unicas
            longitud = len(palabra)
            if longitud not in grupos:        # crear la clave antes del append
                grupos[longitud] = []
            grupos[longitud].append(palabra)
        return grupos

    def palabras_unicas(self):
        """Retorna el CONJUNTO de palabras distintas analizadas."""
        return set(self.palabras)


# --- Programa principal ---
if __name__ == "__main__":
    ap = AnalizadorPatrones()

    texto = "el gato esta aqui"

    print("agrupar_por_longitud ->", ap.agrupar_por_longitud(texto))
    print("palabras con 'a'     ->", ap.encontrar_palabras(texto, "a"))
    print("palabras unicas      ->", ap.palabras_unicas())
    print("cuantas unicas       ->", len(ap.palabras_unicas()))


# =============================================================================
# BOSQUEJO A MANO - asi se ejecuta paso a paso
# =============================================================================
# agrupar_por_longitud("el gato esta aqui")
#   palabras = texto.split() -> ['el', 'gato', 'esta', 'aqui']
#   grupos = {}
#
#   'el'   -> len = 2 -> la clave 2 no existe -> grupos = {2: ['el']}
#   'gato' -> len = 4 -> la clave 4 no existe -> grupos = {2:['el'], 4:['gato']}
#   'esta' -> len = 4 -> la clave 4 YA existe -> se APILA
#                        grupos = {2:['el'], 4:['gato','esta']}
#   'aqui' -> len = 4 -> se apila tambien
#                        grupos = {2:['el'], 4:['gato','esta','aqui']}
#
# encontrar_palabras(texto, "a")
#   'el'   -> startswith("a") ? NO
#   'gato' -> NO
#   'esta' -> NO
#   'aqui' -> SI -> ['aqui']
#
# palabras_unicas()
#   set(palabras) = {'el','gato','esta','aqui'} -> 4 palabras distintas
