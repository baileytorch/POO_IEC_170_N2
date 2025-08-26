import datetime
from modelo.libro import Libro
from modelo.lector import Lector


class Prestamo(Libro, Lector):  # type: ignore
    def __init__(self, id_prestamo=0, id_libro=0, id_lector=0, fecha_prestamo=datetime.datetime.now(), fecha_devolucion=datetime.datetime.now(), fecha_entrega=datetime.datetime.now()):
        Libro().__init__(id_libro)  # type: ignore
        Lector().__init__(id_lector)  # type: ignore
        self.id_prestamo = id_prestamo
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.fecha_entrega = fecha_entrega
