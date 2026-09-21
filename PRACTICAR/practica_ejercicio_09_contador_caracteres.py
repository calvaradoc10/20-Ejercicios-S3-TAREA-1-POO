# EJERCICIO 09 - Contador de mayusculas, minusculas y numeros

class ContadorCaracteres:
    """Cuenta los tipos de caracteres de un texto."""

    def __init__(self):
        self.ultimo_texto = ""

    def es_mayuscula(self, caracter):
        """Retorna True si el caracter es mayuscula."""
        return caracter.isupper()

    def contar_tipos(self, texto):
        """Cuenta mayusculas, minusculas y numeros del texto."""
        conteo = {"mayusculas": 0, "minusculas": 0, "numeros": 0}
        for caracter in texto:
            if self.es_mayuscula(caracter):
                conteo["mayusculas"] += 1
            elif caracter.islower():
                conteo["minusculas"] += 1
            elif caracter.isdigit():
                conteo["numeros"] += 1
        self.ultimo_texto = texto
        return conteo


# Programa
if __name__ == "__main__":
    cc = ContadorCaracteres()

    print("Es mayuscula? ", cc.es_mayuscula("p"))
    print("Conteo: ", cc.contar_tipos("Python3 Es Facil 100"))
    print("Ultimo texto: ", cc.ultimo_texto)
