class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome.ljust(25)} | {self.categoria.ljust(25)} | {self.ativo}'

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
