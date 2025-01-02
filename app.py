import os

from Restaurante import Restaurante

def ativar_restaurante():
    exibir_subtitulo("Alterar estado de ativo do restaurante")
    nome = input("Digite o nome de um restaurante:\n")
    restaurante_encontrado = False
    for restaurante in Restaurante.restaurantes:
        if nome == restaurante.nome:
            restaurante_encontrado = True
            restaurante._ativo = not restaurante._ativo
            msg = f'O restaurante {nome} foi ativado!' if restaurante._ativo else f'O restaurante {nome} foi desativado!'
            print(msg)
    if not restaurante_encontrado:
        print("Restaurante não encontrado!\n")
    voltar_menu()

def exibir_subtitulo(texto):
    os.system('clear')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()


def exibir_nome_programa():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝\n\n""")


def exibir_opcs():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair')


def voltar_menu():
    input("\nPressione Enter para voltar ao menu principal!\n")
    main()


def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes")
    restaurante_nome = input("Digite o nome do restaurante:\n")
    restaurante_categoria = input("Digite a categoria desse restaurantes:\n")
    restaurante = Restaurante(restaurante_nome, restaurante_categoria)
    # dados_restaurante = {'nome': restaurante.nome, 'categoria': restaurante.categoria, 'ativo': restaurante.ativo}
    print(f'\nRestaurante {restaurante.nome} adicionado com sucesso à lista!\n')
    voltar_menu()


def listar_restaurantes():
    exibir_subtitulo("Lista de restaurantes cadastrados")
    for restaurante in Restaurante.restaurantes:
        print(restaurante)
    voltar_menu()


def finalizar_app():
    os.system('clear')
    print('Finalizando app...')


def opc_invalida():
    print("Digite uma opção válida!\n")
    voltar_menu()


def escolher_opc():
    try:
        opc = int(input("O que você deseja fazer?\n"))

        if opc == 1:
            cadastrar_novo_restaurante()
        elif opc == 2:
            listar_restaurantes()
        elif opc == 3:
            ativar_restaurante()
        elif opc == 4:
            finalizar_app()
        else:
            opc_invalida()

    except:
        opc_invalida()


def main():
    os.system('clear')
    exibir_nome_programa()
    exibir_opcs()
    escolher_opc()


if __name__ == '__main__':
    main()
