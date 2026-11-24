class Vista:
    def menu(self):
        print("\n--- FUNDACION MANOS UNIDAS ---")
        print("1. Registrar kit")
        print("2. Mostrar kits")
        print("3. Entregar kits")
        print("4. Salir")
        return int(input("Opcion: "))

    def registrar(self):
        nombre = input("Nombre: ")
        contenido = input("Contenido: ")
        unidades = int(input("Unidades: "))
        return nombre, contenido, unidades

    def mostrar(self, kits):
        print(f"{'Codigo':<8}{'Nombre':<20}{'Contenido':<25}{'Unidades'}")

        for kit in kits:
            print(kit)

    def pedirCodigo(self):
        return int(input("Codigo: "))

    def pedirCantidad(self):
        return int(input("Cantidad: "))

    def mensaje(self, texto):
        print(texto)