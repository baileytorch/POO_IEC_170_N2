from modelo.direccion import Direccion
from modelo.biblioteca import Biblioteca


class Lector(Direccion, Biblioteca):  # type: ignore
    def __init__(self, id_lector=0, id_direccion=0, id_biblioteca=0, rut=0, digito_verificador='', nombre_lector='', habilitado=True):
        super().__init__(id_direccion)  # type: ignore
        super().__init__(id_biblioteca)  # type: ignore
        self.id_lector = id_lector
        self.rut = rut
        self.digito_verificador = digito_verificador
        self.nombre_lector = nombre_lector
        self.habilitado = habilitado
