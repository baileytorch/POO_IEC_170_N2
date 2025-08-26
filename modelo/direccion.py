from modelo.comuna import Comuna


class Direccion(Comuna):
    def __init__(self, id_direccion=0, id_comuna=0, calle='', numero='', departamento=''):
        super().__init__(id_comuna)  # type: ignore
        self.id_direccion = id_direccion
        self.calle = calle
        self.numero = numero
        self.departamento = departamento
