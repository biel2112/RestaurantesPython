from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    '''
    Inicializa uma instância de itens de um cardápio e será uma classe
    que fornecerá atributos a serem herdados por outras classes (Prato e Bebida)

    '''
    def __init__(self, nome, preco):
        self._nome = nome.title()
        self._preco = preco

    @property
    def nome(self):
        '''
        Estabelece como o atributo "nome" do cardápio deve ser retornado

        '''
        return self._nome

    @property
    def preco(self):
        '''
        Estabelece como o atributo "preco" do cardápio deve ser retornado

        '''
        return self._preco

    @abstractmethod
    def aplicar_desconto(self):
        '''
        Estabelece um método abstrato de aplicar desconto;

        As classes herdadas devem estabelecer o valor do desconto que deve ser retornado;
        '''
        pass
