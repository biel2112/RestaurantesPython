class ItemCardapio:
    def __init__(self, nome, preco):
        self._nome = nome.title()
        self._preco = preco

    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco