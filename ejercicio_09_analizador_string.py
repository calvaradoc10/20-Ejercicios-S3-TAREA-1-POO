# =============================================================================
# EJERCICIO 09 - Validador de caracteres
# =============================================================================

class AnalizadorString:
    """Cuenta vocales, consonantes y digitos de un texto."""

    def __init__(self):
        self.texto_mas_largo = ""   # atributo pedido por el enunciado

    def solo_vocales(self, letra):
        """Retorna True si la letra es una vocal."""
        return letra.lower() in "aeiou"

    def contar_por_tipo(self, texto):
        """Clasifica cada caracter del texto en vocal, consonante o digito."""
        conteo = {"vocales": 0, "consonantes": 0, "digitos": 0}

        for caracter in texto:
            if caracter.isdigit():
                conteo["digitos"] += 1
            elif caracter.isalpha():
                if self.solo_vocales(caracter):        # REUTILIZACION
                    conteo["vocales"] += 1
                else:
                    conteo["consonantes"] += 1
            # los espacios y signos no se cuentan

        # actualizo el texto mas largo analizado
        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        return conteo


# --- Programa principal ---
if __name__ == "__main__":
    astr = AnalizadorString()

    print("solo_vocales('H')          ->", astr.solo_vocales("H"))
    print("contar_por_tipo('Hola123') ->", astr.contar_por_tipo("Hola123"))
    print("Texto mas largo analizado  ->", astr.texto_mas_largo)


# =============================================================================
# BOSQUEJO A MANO - asi se ejecuta paso a paso
# =============================================================================
# conteo = {"vocales": 0, "consonantes": 0, "digitos": 0}
# texto  = "Hola123"
#
# 'H' -> es letra; solo_vocales('H') -> 'h' no esta en "aeiou" -> consonantes = 1
# 'o' -> es vocal                                              -> vocales     = 1
# 'l' -> consonante                                            -> consonantes = 2
# 'a' -> vocal                                                 -> vocales     = 2
# '1' -> isdigit() True                                        -> digitos     = 1
# '2' -> digito                                                -> digitos     = 2
# '3' -> digito                                                -> digitos     = 3
#
# return {"vocales": 2, "consonantes": 2, "digitos": 3}
#
# texto_mas_largo: len("Hola123") = 7 > 0 -> se guarda "Hola123"
