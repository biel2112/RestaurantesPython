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
        self.tamanho = tamanho