import os

"""Importa a classe restaurante para a variável rest"""
from modelos.restaurante import Restaurante as rest


def exibir_nome_programa():
    """Exibe o nome do programa"""
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝\n\n""")

def exibir_subtitulo(texto):
    """Forma um título contornado de asteriscos com o texto recebido

        Parâmetros:
        - texto (str): Texto a ser transformado em subtítulo
    """
    os.system('clear')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()





def exibir_opcs():
    """Exibe uma lista de opções de ação do menu principal"""
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Avaliar restaurante')
    print('5. Cadastrar item ao cardápio do restaurante')
    print('6. Ver cardápio de algum restaurante')
    print('7. Sair')

def buscar_restaurante(restaurante):
    try:
        return next(r for r in rest.restaurantes if r.nome.lower() == restaurante.lower())
    except StopIteration:
        print(f"Restaurante '{restaurante}' não encontrado!\n")
        return None

def voltar_menu():
    "Retorna para o Menu Principal após pressionar a tecla Enter"
    input("\nPressione Enter para voltar ao menu principal!\n")
    main()

def finalizar_app():
    """Encerra o aplicativo"""
    os.system('clear')
    print('Finalizando app...')


def opc_invalida():
    """Mensagem mostrada ao pressionar uma opção inexistente do menu principal"""
    print("Digite uma opção válida!\n")
    voltar_menu()

def escolher_opc():
    """Retorna as ações escolhidas pelo usuário no menu principal"""
    try:
        opc = int(input("O que você deseja fazer?\n"))

        if opc == 1:
            exibir_subtitulo("Cadastro de novos restaurantes")
            rest.cadastrar_novo_restaurante()
            voltar_menu()

        elif opc == 2:
            exibir_subtitulo("Lista de restaurantes cadastrados")
            rest.listar_restaurantes()

            voltar_menu()


        elif opc == 3:
            exibir_subtitulo("Alterar estado de ativo do restaurante")
            nome_restaurante = input("Digite o nome do restaurante a ser ativado/desativado:\n")
            try:
                restaurante = buscar_restaurante(nome_restaurante)
                restaurante.ativar_restaurante()

            except StopIteration:
                print(f"Restaurante '{nome_restaurante}' não encontrado!\n")

            voltar_menu()

        elif opc == 4:
            exibir_subtitulo("Área de avaliação de restaurantes")
            nome_restaurante = input("Digite o nome do restaurante a ser avaliado:\n")
            try:
                restaurante = buscar_restaurante((nome_restaurante))
                nome_cliente = input("Digite seu nome:\n")
                nota = float(input("Digite a nota (0.0 a 10.0):\n"))
                restaurante.avaliar(nome_cliente, nota)
            except StopIteration:
                print(f"Restaurante '{nome_restaurante}' não encontrado!\n")
            except ValueError:
                print("Nota inválida. Digite um número entre 0.0 e 10.0")
            voltar_menu()

        elif opc == 5:
            exibir_subtitulo("Adicionar item ao cardápio dor restaurante")
            nome_restaurante = input("Digite o nome do restaurante que deseja adicionar um item no cardápio:\n")
            try:
                restaurante = buscar_restaurante(nome_restaurante)
                restaurante.adicionar_item_cardapio()

            except StopIteration:
                print(f"Restaurante '{nome_restaurante}' não encontrado!\n")

            voltar_menu()

        elif opc == 6:
            exibir_subtitulo("Ver cardápio do restaurante")
            nome_restaurante = input("Digite o nome do restaurante que deseja fazer seu pedido:\n")
            try:
                restaurante = buscar_restaurante((nome_restaurante))
                restaurante.listar_itens_cardapio()
            except StopIteration:
                print(f"Restaurante '{nome_restaurante}' não encontrado!\n")
            voltar_menu()

        elif opc == 7:
            finalizar_app()

        else:
            opc_invalida()

    except:
        opc_invalida()

def main():
    """Roda o programa"""
    os.system('clear')
    exibir_nome_programa()
    exibir_opcs()
    escolher_opc()

if __name__ == '__main__':
    main()
