from modelos.avaliacao import Avaliacao
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato


class Restaurante:
    """Representa um restaurante e suas características."""

    restaurantes = []

    def __init__(self, nome, categoria):
        """
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._pratos = []
        self._bebidas = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        """Retorna uma representação em string do restaurante."""
        return f'{self._nome.ljust(25)} | {self._categoria.ljust(25)} | {str(self.media_avaliacao).ljust(25)} | {self.ativo}'

    @classmethod
    def listar_restaurantes(cls):
        """Exibe uma lista formatada de todos os restaurantes com os cabeçalhos."""
        print(f'{"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(restaurante)

    @classmethod
    def cadastrar_novo_restaurante(cls):
        """Cadastra um restaurante e forma uma instância com os dados fornecidos (nome e categoria)"""
        restaurante_nome = input("Digite o nome do restaurante:\n")
        restaurante_categoria = input("Digite a categoria desse restaurantes:\n")
        restaurante = Restaurante(restaurante_nome, restaurante_categoria)
        print(f'\nRestaurante {restaurante._nome} adicionado com sucesso à lista!\n')

    def ativar_restaurante(self):
        """Alterna o estado de atividade do restaurante."""
        self._ativo = not self._ativo
        msg = f'O restaurante {self.nome} foi ativado!' if self._ativo else f'O restaurante {self.nome} foi desativado!'
        print(msg)

    def avaliar(self, nome_cliente, nota):
        """Recebe uma nota e adiciona ao array de avaliações

        Parâmetros:
        - nome_cliente (str): Nome do cliente que irá avaliar o restaurante
        - nota (float): Nota da avaliação do restaurante a ser digitada pelo cliente
        """
        avaliacao = Avaliacao(nome_cliente, nota)
        self._avaliacao.append(avaliacao)
        print("Avaliação realizada com sucesso!")



    @property
    def media_avaliacao(self):
        """Calcula e retorna a média dos valores do array de avaliações do restaurante pesquisado"""
        if not self._avaliacao:
            return 0
        else:
            soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
            qtd_notas = len(self._avaliacao)
            media_notas = round(soma_notas/qtd_notas, 1)
            return media_notas

    @property
    def ativo(self):
        """Retorna um símbolo indicando o estado de atividade do restaurante."""
        return '⌧' if self._ativo else '☐'

    @property
    def nome(self):
        """Retorna o valor do nome do atributo da instância da classe Restaurante """
        return self._nome

    def adicionar_item_cardapio(self):
        opc = 0
        while opc != 3:
            opc = int(input("""
                    Digite o número do que deseja adicionar no cardápio deste restaurante:
                    1 - Prato
                    2 - Bebida
                    3 - Sair
                    """))
            if opc == 1:

                nome_prato = input("Digite o nome do prato que deseja cadastrar:\n")
                preco_prato = float(input("Digite o preço desse prato\n"))
                descricao_prato = input("Digite uma descrição sobre esse prato\n")

                prato = Prato(nome_prato, preco_prato, descricao_prato)
                self._pratos.append(prato)
                print("Prato cadastrado com sucesso!\n")

            elif opc == 2:
                nome_bebida = input("Digite o nome da bebida que deseja cadastrar:\n")
                preco_bebida = float(input("Digite o preço dessa bebida\n"))
                tamanhos_bebida = input("Digite os tamanhos disponíveis para essa bebida\n")

                bebida = Bebida(nome_bebida, preco_bebida, tamanhos_bebida)
                self._bebidas.append(bebida)
                print("Bebida cadastrada com sucesso!\n")

            elif opc < 1 or opc > 3:
                print("Digite uma opção válida!")

    def listar_itens_cardapio(self):
        opc = 0
        while opc != 4:
            opc = int(input("""
                    Digite o número do que deseja ver do cardápio deste restaurante:
                    1 - Pratos
                    2 - Bebidas
                    3 - Fazer Pedido
                    4 - Sair
                    """))
            if opc == 1:
                if self._pratos:
                    print(f'{"Prato".ljust(25)} | {"Preço".ljust(25)} | {"Descrição"}')
                    for prato in self._pratos:
                        print(prato)
                else:
                    print("Sem pratos cadastrados para este restaurante!")

            elif opc == 2:
                if self._bebidas:
                    print(f'{"Bebida".ljust(25)} | {"Preço".ljust(25)} | {"Tamanho"}')
                    for bebida in self._bebidas:
                        print(bebida)
                else:
                    print("Sem bebidas cadastradas para este restaurante!")

            elif opc == 3:
                self.escolher_item_cardapio()
                break

            elif opc < 1 or opc > 4:
                print("Digite uma opção válida!")

    def escolher_item_cardapio(self):
        conta = []
        opc = 0
        while opc != 4:
            opc = int(input("""
            Digite o número do que deseja escolher:
            
            1 - Prato
            2 - Bebida
            3 - Pagar
            4 - Sair
            
            """))
            if opc == 1:
                if not self._pratos:
                    print("Nenhum prato disponível no cardápio.")
                    continue
                nome_prato = input("Digite o nome do prato que deseja escolher:\n").strip()
                prato = next((p for p in self._pratos if p.nome.lower() == nome_prato.lower()), None)
                if prato:
                    opc_desconto = int(input("""Deseja aplicar desconto?
                                        1 - Sim
                                        2 - Não
                                        """))
                    while opc_desconto == 1 or opc_desconto == 2:
                        if opc_desconto == 1:
                            prato.aplicar_desconto()
                            conta.append(prato.preco)
                            for valor in conta:
                                print(valor)
                            print(f"Prato '{prato.nome}' adicionado à sua conta.")
                            break

                        elif opc_desconto == 2:
                            conta.append(prato.preco)
                            for valor in conta:
                                print(valor)
                            print(f"Prato '{prato.nome}' adicionado à sua conta.")
                            break
                else:
                    print("Prato não encontrado.")

            elif opc == 2:
                if not self._bebidas:
                    print("Nenhuma bebida disponível no cardápio.")
                    continue
                nome_bebida = input("Digite o nome da bebida que deseja escolher:\n").strip()
                bebida = next((b for b in self._bebidas if b.nome.lower() == nome_bebida.lower()), None)
                if bebida:
                    opc_desconto = int(input("""Deseja aplicar desconto?
                    1 - Sim
                    2 - Não
                    """))
                    while opc_desconto == 1 or opc_desconto == 2:
                        if opc_desconto == 1:
                            bebida.aplicar_desconto()
                            conta.append(bebida.preco)
                            print(f"Bebida '{bebida.nome}' adicionada à sua conta.")
                            break

                        elif opc_desconto == 2:
                            conta.append(bebida.preco)
                            print(f"Bebida '{bebida.nome}' adicionada à sua conta.")
                            break
                else:
                    print("Bebida não encontrada.")

            elif opc == 3:
                total_conta = sum(conta)
                print(f'O total a pagar será de: {total_conta:.2f}')
                conta = []

            elif opc == 4:
                conta = []

            elif opc < 1 or opc > 4:
                print("Digite uma opção válida")