class Controlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar(self):
        opcion = 0

        while opcion != 4:
            try:
                opcion = self.vista.menu()
            except ValueError:
                self.vista.mensaje("Ingrese un numero valido")
                continue

            if opcion == 1:
                try:
                    nombre, contenido, unidades = self.vista.registrar()
                    codigo = self.modelo.registrar(nombre, contenido, unidades)
                    self.vista.mensaje(f"Registrado con el codigo {codigo}.")
                except ValueError as error:
                    self.vista.mensaje(str(error))

            elif opcion == 2:
                kits = self.modelo.mostrar()
                self.vista.mostrar(kits)

            elif opcion == 3:
                try:
                    codigo = self.vista.pedirCodigo()
                    self.modelo.buscar(codigo)
                    cantidad = self.vista.pedirCantidad()
                    unidades = self.modelo.entregar(codigo, cantidad)
                    self.vista.mensaje(f"listo. Quedan {unidades} kits.")
                except ValueError as error:
                    self.vista.mensaje(str(error))

            elif opcion == 4:
                self.vista.mensaje("programa finalizado")
