from modelo.autor import Autor
from modelo.biblioteca import Biblioteca
from modelo.categoria import Categoria


class Libro(Autor, Biblioteca, Categoria):
    def __init__(self, id_libro=0, titulo='', id_autor=0, paginas=0, copias=0, id_biblioteca=0, habilitado=True, id_categoria=0):
        super().__init__(id_autor)  # type: ignore
        super().__init__(id_biblioteca)  # type: ignore
        super().__init__(id_categoria)  # type: ignore
        self.id_libro = id_libro
        self.titulo = titulo
        self.paginas = paginas
        self.copias = copias
        self.habilitado = habilitado
