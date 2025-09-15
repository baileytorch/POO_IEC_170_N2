from modelo.direccion import Direccion


class Biblioteca(Direccion):
    def __init__(self, id_biblioteca=0, id_direccion=0, nombre_biblioteca='', habilitado=True):
        super().__init__(id_direccion)  # type: ignore
        self.id_biblioteca = id_biblioteca
        self.nombre_biblioteca = nombre_biblioteca
        self.habilitado = habilitado
