from modelos.avaliacao import Avaliacao

class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome.ljust(25)} | {self._categoria.ljust(25)} | {str(self.media_avaliacao).ljust(25)} | {self.ativo}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status"}')
        for restaurante in Restaurante.restaurantes:
            print(restaurante)

    @classmethod
    def cadastrar_novo_restaurante(cls):
        restaurante_nome = input("Digite o nome do restaurante:\n")
        restaurante_categoria = input("Digite a categoria desse restaurantes:\n")
        restaurante = Restaurante(restaurante_nome, restaurante_categoria)
        print(f'\nRestaurante {restaurante._nome} adicionado com sucesso à lista!\n')

    def ativar_restaurante(self):  # Método de instância
        self._ativo = not self._ativo
        msg = f'O restaurante {self.nome} foi ativado!' if self._ativo else f'O restaurante {self.nome} foi desativado!'
        print(msg)

    def avaliar(self, nome_cliente, nota):  # Método de instância
        avaliacao = Avaliacao(nome_cliente, nota)
        self._avaliacao.append(avaliacao)
        print("Avaliação realizada com sucesso!")



    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return 0
        else:
            soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
            qtd_notas = len(self._avaliacao)
            media_notas = round(soma_notas/qtd_notas, 1)
            return media_notas

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'

    @property
    def nome(self):
        return self._nome

