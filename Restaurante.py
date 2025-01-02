class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'-{self.nome.ljust(20)} | {self.categoria.ljust(20)} | {self.ativo}'

    @property
    def ativo(self):
        return '☐' if self._ativo else '⌧'
