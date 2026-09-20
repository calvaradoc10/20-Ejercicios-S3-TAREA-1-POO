# EJERCICIO 10 - Gestor de tareas con prioridad
class Tareas:
    """Gestor de tareas guardadas como lista de tuplas."""

    def __init__(self):
        self.tareas = []   # lista de tuplas (descripcion, prioridad)

    def agregar_tarea(self, descripcion, prioridad):
        """Guarda la tarea como una TUPLA dentro de la lista."""
        self.tareas.append((descripcion, prioridad))
        return self.tareas

    def tareas_prioritarias(self):
        """Retorna solo las tareas con prioridad alta."""
        prioritarias = []
        for descripcion, prioridad in self.tareas:   # desempaquetado de tupla
            if prioridad.lower() == "alta":
                prioritarias.append((descripcion, prioridad))
        return prioritarias

    def eliminar_completada(self, descripcion):
        """Elimina una tarea por su descripcion."""
        pendientes = []
        for tarea in self.tareas:
            if tarea[0] != descripcion:     # conserva las que no coinciden
                pendientes.append(tarea)
        self.tareas = pendientes
        return self.tareas


# Programa
if __name__ == "__main__":
    t = Tareas()

    t.agregar_tarea("Estudiar", "alta")
    t.agregar_tarea("Leer", "baja")

    print("Todas las tareas: ", t.tareas)
    print("Tareas prioritarias: ", t.tareas_prioritarias())
    print("Tras borrar 'Leer': ", t.eliminar_completada("Leer"))


# BOSQUEJO A MANO paso a paso
# self.tareas = []         lista de TUPLAS (descripcion, prioridad)
#
# agregar_tarea("Estudiar", "alta")
#   tareas = [("Estudiar", "alta")]
#
# agregar_tarea("Leer", "baja")
#   tareas = [("Estudiar","alta"), ("Leer","baja")]
#
# tareas_prioritarias()
#   ("Estudiar","alta")   prioridad == "alta" ?    SI  ->  [("Estudiar","alta")]
#   ("Leer","baja")       "baja" == "alta"    ?    NO  ->  no entra
#   return [("Estudiar","alta")]
#
# eliminar_completada("Leer")
#   recorro y me quedo con las que no se llaman "Leer"
#   ("Estudiar","alta")    se conserva
#   ("Leer","baja")        se elimina
#   tareas = [("Estudiar","alta")]
