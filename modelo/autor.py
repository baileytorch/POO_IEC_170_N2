from modelo.nacionalidad import Nacionalidad


class Autor(Nacionalidad):
    def __init__(self, id_autor=0, nombre_autor='', pseudonimo='', id_nacionalidad=0, habilitado=True):
        super().__init__(id_nacionalidad)  # type: ignore
        self.id_autor = id_autor
        self.nombre_autor = nombre_autor
        self.pseudonimo = pseudonimo
        self.habilitado = habilitado
