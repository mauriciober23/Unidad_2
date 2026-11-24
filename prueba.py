class kit:
    def __init__(self,codigo,nombre,contenido,unidades):
        self.codigo = codigo
        self.nombre = nombre
        self.contenido = contenido
        self.unidades = unidades
    def entregar(self,cantidad):
        if cantidad <= 0 or cantidad > self.unidades:
            print("error cantidad no valida")
            return False
        self.unidades -= cantidad
        return True
    def __init__(self


                 



