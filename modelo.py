class Kit:
    def __init__(self, codigo, nombre, contenido, unidades):
        self.codigo = codigo
        self.nombre = nombre
        self.contenido = contenido
        self.unidades = unidades

    def entregar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("Error: cantidad no valida.")

        if cantidad > self.unidades:
            raise ValueError(f"Error: solo hay {self.unidades} kits.")

        self.unidades -= cantidad
        return True

    def __str__(self):
        return f"{self.codigo:<8}{self.nombre:<20}{self.contenido:<25}{self.unidades}"


class Modelo:
    def __init__(self):
        self.kits = [
            Kit(1, "Kit escolar", "Cuadernos y lápices", 50),
            Kit(2, "Kit de aseo", "Jabón y pasta dental", 40)
        ]

    def registrar(self, nombre, contenido, unidades):
        if unidades <= 0:
            raise ValueError("Error: las unidades deben ser mayores a cero.")

        codigo = len(self.kits) + 1
        self.kits.append(Kit(codigo, nombre, contenido, unidades))
        return codigo

    def buscar(self, codigo):
        for kit in self.kits:
            if kit.codigo == codigo:
                return kit

        raise ValueError("Error: no existe ese código.")

    def entregar(self, codigo, cantidad):
        kit = self.buscar(codigo)
        kit.entregar(cantidad)
        return kit.unidades

    def mostrar(self):
        return self.kits