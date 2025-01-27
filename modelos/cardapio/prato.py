from abc import ABC

from modelos.cardapio.item_cardapio import ItemCardapio


class Prato(ItemCardapio, ABC):
    '''
    Inicializa uma instância de Prato

    Parâmetros:
            - nome (str): Nome do prato (Herdado da classe ItemCardapio)
            - preco (float): Preço do prato (Herdado da classe ItemCardapio)
            - descricao (str): descricao do prato
    '''
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao

    def __str__(self):

        '''Retorna uma representação em string de uma instância da classe de Prato'''

        return f'{self._nome.ljust(25)} | {str(self._preco).ljust(25)} | {self._descricao}'

    def aplicar_desconto(self):

        '''
        Aplica um desconto no preço da instância da classe Prato recebida
        no parâmetro desta função
        '''

        self._preco -= (self._preco * 0.05)

