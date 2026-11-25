class Controlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar(self):
        opcion = ""

        while opcion != "4":
            opcion = self.vista.menu()

            if opcion == "1":
                try:
                    nombre, contenido, unidades = self.vista.registrar()

                    if unidades <= 0:
                        raise ValueError("Error: las unidades deben ser mayores a cero.")

                    codigo = self.modelo.registrar(nombre, contenido, unidades)
                    self.vista.mensaje(f"Registrado con el codigo {codigo}.")

                except ValueError as error:
                    self.vista.mensaje(str(error))

            elif opcion == "2":
                kits = self.modelo.mostrar()
                self.vista.mostrar(kits)

            elif opcion == "3":
                try:
                    codigo = self.vista.pedirCodigo()
                    kit = self.modelo.buscar(codigo)

                    if kit is None:
                        raise ValueError("Error: no existe ese codigo.")

                    cantidad = self.vista.pedirCantidad()

                    if cantidad <= 0:
                        raise ValueError("Error: cantidad no valida.")

                    if cantidad > kit.unidades:
                        raise ValueError(f"Error: solo hay {kit.unidades} kits.")

                    self.modelo.entregar(codigo, cantidad)
                    self.vista.mensaje(f"Listo. Quedan {kit.unidades} kits.")

                except ValueError as error:
                    self.vista.mensaje(str(error))

            elif opcion == "4":
                self.vista.mensaje("Programa finalizado")

            else:
                self.vista.mensaje("Opcion no valida.")