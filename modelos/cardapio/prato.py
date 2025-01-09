from abc import ABC

from modelos.cardapio.item_cardapio import ItemCardapio


class Prato(ItemCardapio, ABC):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao

    def __str__(self):

        return f'{self._nome.ljust(25)} | {str(self._preco).ljust(25)} | {self._descricao}'

        return f'{self._nome.ljust(25)} | {str(self._preco).ljust(25)} | {self._descricao}'

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)

