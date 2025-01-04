class Avaliacao:
    def __init__(self, cliente, nota):
        """Inicializa uma instância de Avaliacao

        Parâmetros:
        - nome_cliente (str): Nome do cliente que irá avaliar o restaurante
        - nota (float): Nota da avaliação do restaurante a ser digitada pelos clientes
        """
        self._cliente = cliente
        self._nota = nota