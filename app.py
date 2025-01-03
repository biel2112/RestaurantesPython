import os

from modelos.restaurante import Restaurante as r

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
    print('4. Avaliar restaurante')
    print('5. Sair')

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
            r.cadastrar_novo_restaurante()
            voltar_menu()

        elif opc == 2:
            exibir_subtitulo("Lista de restaurantes cadastrados")
            r.listar_restaurantes()
            voltar_menu()

        elif opc == 3:
            exibir_subtitulo("Alterar estado de ativo do restaurante")
            r.ativar_restaurante()
            voltar_menu()

        elif opc == 4:
            exibir_subtitulo("Área de avaliação de restaurantes")
            nome_restaurante = input("Digite o nome do restaurante a ser avaliado:\n")
            try:
                restaurante = next(r for r in r.restaurantes if r.nome.lower() == nome_restaurante.lower())
                nome_cliente = input("Digite seu nome:\n")
                nota = float(input("Digite a nota (0.0 a 10.0):\n"))
                restaurante.avaliar(nome_cliente, nota)  # Chama o método de instância
            except StopIteration:
                print(f"Restaurante '{nome_restaurante}' não encontrado!\n")
            except ValueError:
                print("Nota inválida. Digite um número entre 0.0 e 10.0")
            voltar_menu()

        elif opc == 5:
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
