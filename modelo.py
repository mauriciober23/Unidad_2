class Kit:
    def __init__(self, codigo, nombre, contenido, unidades):
        self.codigo = codigo
        self.nombre = nombre
        self.contenido = contenido
        self.unidades = unidades

    def entregar(self, cantidad):
        if cantidad <= 0 or cantidad > self.unidades:
            return False

        self.unidades -= cantidad
        return True

    def __str__(self):
        return f"{self.codigo:<8}{self.nombre:<20}{self.contenido:<25}{self.unidades}"


class Modelo:
    def __init__(self):
        self.kits = [
            Kit(1, "Kit escolar", "Cuadernos y lapices", 50),
            Kit(2, "Kit de aseo", "Jabon y pasta dental", 40)
        ]

    def registrar(self, nombre, contenido, unidades):
        if unidades <= 0:
            return None

        codigo = len(self.kits) + 1
        self.kits.append(Kit(codigo, nombre, contenido, unidades))
        return codigo

    def buscar(self, codigo):
        for kit in self.kits:
            if kit.codigo == codigo:
                return kit

        return None

    def entregar(self, codigo, cantidad):
        kit = self.buscar(codigo)

        if kit is not None:
            return kit.entregar(cantidad)

        return False

    def mostrar(self):
        return self.kits