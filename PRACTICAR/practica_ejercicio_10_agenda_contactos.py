# EJERCICIO 10 - Agenda de contactos

class Agenda:
    """Guarda contactos como tuplas (nombre, telefono) dentro de una lista."""

    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, telefono):
        """Guarda el contacto como una tupla."""
        self.contactos.append((nombre, telefono))
        return self.contactos

    def buscar_telefono(self, nombre):
        """Retorna el telefono del contacto, o None si no existe."""
        for nombre_guardado, telefono in self.contactos:
            if nombre_guardado == nombre:
                return telefono
        return None

    def eliminar_contacto(self, nombre):
        """Elimina el contacto con ese nombre."""
        nueva = []
        for contacto in self.contactos:
            if contacto[0] != nombre:
                nueva.append(contacto)
        self.contactos = nueva
        return self.contactos


# Programa
if __name__ == "__main__":
    a = Agenda()

    a.agregar_contacto("Carlos", "0993334444")
    a.agregar_contacto("Marta", "0985556666")

    print("Contactos: ", a.contactos)
    print("Telefono de Marta: ", a.buscar_telefono("Marta"))
    print("Telefono de Juan: ", a.buscar_telefono("Juan"))
    print("Tras borrar a Carlos: ", a.eliminar_contacto("Carlos"))
