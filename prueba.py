class Kit:
    def __init__(self, codigo, nombre, contenido, unidades):
        self.codigo = codigo
        self.nombre = nombre
        self.contenido = contenido
        self.unidades = unidades

    def entregar(self, cantidad):
        if cantidad <= 0 or cantidad > self.unidades:
            print("Error: cantidad no valida")
            return False

        self.unidades -= cantidad
        return True

    def __str__(self):
        return f"Codigo: {self.codigo}, Nombre: {self.nombre}, Contenido: {self.contenido}, Unidades: {self.unidades}"


kits = [
    Kit(1, "Kit escolar", "Cuadernos y lapices", 50),
    Kit(2, "Kit de aseo", "Jabon y pasta dental", 40)
]

while True:
    print("\n--- FUNDACION MANOS UNIDAS ---")
    print("1. Registrar kit")
    print("2. Mostrar kits")
    print("3. Entregar kits")
    print("4. Salir")

    try:
        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            codigo = len(kits) + 1
            nombre = input("Nombre del kit: ")
            contenido = input("Contenido: ")
            unidades = int(input("Unidades: "))

            if unidades <= 0:
                print("Error: las unidades deben ser mayores a cero")
            else:
                kits.append(Kit(codigo, nombre, contenido, unidades))
                print("Kit registrado correctamente")

        elif opcion == 2:
            for kit in kits:
                print(kit)

        elif opcion == 3:
            codigo = int(input("Codigo del kit: "))
            encontrado = False

            for kit in kits:
                if kit.codigo == codigo:
                    encontrado = True
                    cantidad = int(input("Cantidad a entregar: "))

                    if kit.entregar(cantidad):
                        print("Listo. Quedan", kit.unidades, "kits")
                    break

            if not encontrado:
                print("Error: no existe ese codigo")

        elif opcion == 4:
            print("Programa finalizado")
            break

        else:
            print("Opcion no valida")

    except ValueError:
        print("Error: ingrese un numero valido")
    except Exception:
        print("Error: dato incorrecto")