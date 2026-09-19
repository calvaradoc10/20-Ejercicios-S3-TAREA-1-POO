# EJERCICIO 01 - Validador de notas con promedio

class Calificador:
    """Valida notas entre 0 y 100 y calcula el promedio de las validas."""

    def __init__(self):
        self.notas = []  #En esta lista se va a guardar las notas validas

    def validar_nota(self, nota):
        """Retorna True si la nota esta entre 0 y 100."""
        return 0 <= nota <= 100

    def cargar_notas(self, *args):
        """Esta funcion recibe varias notas, valida cada una y guarda solo las validas."""
        for nota in args:                      # args es una tupla
            if self.validar_nota(nota):        # REUTILIZACION del metodo validador
                self.notas.append(nota)
        return self.notas

    def promedio(self):
        """Retorna el promedio de las notas guardadas."""
        if len(self.notas) == 0:               # evita division entre cero
            return 0
        return sum(self.notas) / len(self.notas)


# Para ejecutar el programa
if __name__ == "__main__":
    c = Calificador()

    print("validar_nota(85): ", c.validar_nota(85))
    print("validar_nota(110): ", c.validar_nota(110))

    validas = c.cargar_notas(85, 92, 110, 78, -5, 88)
    print("Notas validas: ", validas)
    print("Promedio: ", c.promedio())


#  --BOSQUEJO A MANO paso a paso--
#
# Estado inicial que deja __init__:
# self.notas = [] 
#
# cargar_notas(85, 92, 110, 78, -5, 88)
#   *args llega como TUPLA: (85, 92, 110, 78, -5, 88)
#
#   vuelta 1 nota = 85    0 <= 85 <= 100 ?  SI   notas = [85]
#   vuelta 2 nota = 92                      SI   notas = [85, 92]
#   vuelta 3 nota = 110   110 <= 100 ?      NO  
#   vuelta 4 nota = 78                      SI   notas = [85, 92, 78]
#   vuelta 5 nota = -5    -5 >= 0 ?         NO   
#   vuelta 6 nota = 88                      SI   notas = [85, 92, 78, 88]
#
#   return [85, 92, 78, 88]
#
#  promedio()
#   suma     = 85 + 92 + 78 + 88 = 343
#   cantidad = len(notas) = 4
#   343 / 4  = 85.75
