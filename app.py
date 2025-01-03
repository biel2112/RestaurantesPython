import os

from Restaurante import Restaurante


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
            exibir_subtitulo("Cadastro de novos restaurantes")
            Restaurante.cadastrar_novo_restaurante()
            voltar_menu()

        elif opc == 2:
            exibir_subtitulo("Lista de restaurantes cadastrados")
            Restaurante.listar_restaurantes()
            voltar_menu()

        elif opc == 3:
            exibir_subtitulo("Alterar estado de ativo do restaurante")
            Restaurante.ativar_restaurante()
            voltar_menu()

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
