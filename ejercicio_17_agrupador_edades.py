# EJERCICIO 17 - Grupo de edades

class AgrupadorEdades:
    """Clasifica edades por categoria y las agrupa en un diccionario."""

    def __init__(self):
        self.grupos = {}

    def clasificar_edad(self, edad):
        """Retorna la categoria a la que pertenece la edad."""
        if edad <= 11:
            return "nino"
        elif edad <= 17:
            return "adolescente"
        elif edad <= 64:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        """Agrupa todas las edades recibidas en un diccionario de listas."""
        for edad in edades:
            categoria = self.clasificar_edad(edad)      
            if categoria not in self.grupos:            
                self.grupos[categoria] = []
            self.grupos[categoria].append(edad)
        return self.grupos

    def edad_promedio_categoria(self, categoria):
        """Promedio de edades de una categoria."""
        if categoria not in self.grupos or len(self.grupos[categoria]) == 0:
            return 0
        lista = self.grupos[categoria]
        return sum(lista) / len(lista)


# Programa
if __name__ == "__main__":
    ae = AgrupadorEdades()

    print("Clasificar edad: ", ae.clasificar_edad(15))
    print("Agrupado: ", ae.agrupar_por_categoria(5, 15, 30, 70))
    print("Promedio de: ", ae.edad_promedio_categoria("nino"))

# BOSQUEJO A MANO paso a paso
# clasificar_edad usa estos rangos:
#    0 a 11  -> "nino"          12 a 17  -> "adolescente"
#   18 a 64  -> "adulto"        65 o mas -> "mayor"
#
# agrupar_por_categoria(5, 15, 30, 70)
#   grupos = {}
#
#   edad = 5  -> clasificar_edad(5)  = "nino"
#                la clave "nino" no existe -> la creo con lista vacia
#                grupos = {"nino": [5]}
#
#   edad = 15 -> "adolescente" -> grupos = {"nino":[5], "adolescente":[15]}
#   edad = 30 -> "adulto"      -> grupos = {..., "adulto":[30]}
#   edad = 70 -> "mayor"       -> grupos = {..., "mayor":[70]}
#
# edad_promedio_categoria("nino")
#   lista [5] ->   5 / 1  = 5.0
