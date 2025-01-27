from modelos.cardapio.item_cardapio import ItemCardapio


class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        """Inicializa uma instância de bebida

            Parâmetros:
            - nome (str): Nome da bebida (Herdado da classe ItemCardapio)
            - preco (float): Preço da bebida (Herdado da classe Item Cardapio)
            - tamanho (str): Tamanho da bebida (P, M ou G)
        """

        super().__init__(nome, preco)
        self._tamanho = tamanho

    def __str__(self):

        '''Retorna uma representação em string de uma instância da classe de Bebida'''

        return f'{self._nome.ljust(25)} | {str(self._preco).ljust(25)} | {self._tamanho}'

    def aplicar_desconto(self):
        '''
        Aplica um desconto no preço da instância da classe Bebida recebida
        no parâmetro desta função
        '''
        self._preco -= (self.preco * 0.1)