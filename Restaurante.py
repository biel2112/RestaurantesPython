class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome.ljust(25)} | {self._categoria.ljust(25)} | {self.ativo}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Status"}')
        for restaurante in Restaurante.restaurantes:
            print(restaurante)

    @classmethod
    def cadastrar_novo_restaurante(cls):
        restaurante_nome = input("Digite o nome do restaurante:\n")
        restaurante_categoria = input("Digite a categoria desse restaurantes:\n")
        restaurante = Restaurante(restaurante_nome, restaurante_categoria)
        print(f'\nRestaurante {restaurante._nome} adicionado com sucesso à lista!\n')

    @classmethod
    def ativar_restaurante(cls):
        nome = input("Digite o nome de um restaurante:\n").lower()
        try:
            restaurante = next(r for r in Restaurante.restaurantes if r.nome.lower() == nome)
            restaurante._ativo = not restaurante._ativo
            msg = f'O restaurante {nome} foi ativado!' if restaurante._ativo else f'O restaurante {nome} foi desativado!'
            print(msg)
        except StopIteration:
            print("Restaurante não encontrado!\n")

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'

    @property
    def nome(self):
        return self._nome

