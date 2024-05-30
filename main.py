from Relacionamento import Relacionamento
import os


def limpa_terminal():
    # garante terminal limpo em qualquer SO
    os.system("cls" if os.name == "nt" else "clear")


def exibir_menu():
    print("\n===== [MENU] =====")
    print("1. Inserir usuário")
    print("2. Remover usuário")
    print("3. Visualizar Relacionamentos")
    print("4. Adicionar Relacionamento")
    print("5. Encontrar Usuário")
    print("6. Encontrar Comunidade")
    print("0. Sair")
    print("==================")


def main():

    redeSocial = Relacionamento()

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            usuario_id = input("Digite o ID do novo usuário: ")
            nome = input("Digite o nome do novo usuário: ")
            redeSocial.adicionar_usuario(usuario_id, nome)
            print("")
            input("Pressione enter para continuar...")
            limpa_terminal()
        elif escolha == '2':
            usuario_id = input("Digite o ID do usuário a ser removido: ")
            redeSocial.remover_usuario(usuario_id)
            print("")
            input("Pressione enter para continuar...")
            limpa_terminal()
        elif escolha == '3':
            print("Estrutura de relacionamentos:")
            redeSocial.mostrar_arvore()
            print("")
            input("Pressione enter para continuar...")
            limpa_terminal()
        elif escolha == '4':
            usuario_id1 = input("Digite o ID do primeiro usuário: ")
            usuario_id2 = input("Digite o ID do segundo usuário: ")
            redeSocial.adicionar_relacionamento(usuario_id1, usuario_id2)
            input("Pressione enter para continuar...")
            limpa_terminal()
        elif escolha == '5':
            usuario_id = input("Digite o ID do usuário a ser encontrado: ")
            usuario = redeSocial.encontrar_usuario(usuario_id)
            if usuario:
                print(f"Usuário encontrado: {usuario.nome} ({usuario.usuario_id})")  # nopep8
            print("")
            input("Pressione enter para continuar...")
            limpa_terminal()
        elif escolha == '6':
            comunidades = redeSocial.encontrar_comunidades()
            for idx, comunidade in enumerate(comunidades):
                print(f"Comunidade {idx + 1}:")
                for usuario in comunidade:
                    print(f"{usuario.nome} ({usuario.usuario_id})")
            print("")
            input("Pressione enter para continuar...")
            limpa_terminal()
        elif escolha == '0':
            print("Saindo...")
            break
        else:
            print("Opção incorreta. Por favor, escolha novamente.")
            input("Pressione enter para continuar...")
            limpa_terminal()

    print("Inserindo 3 usuários...")
    redeSocial.adicionar_usuario(1, "Alice")
    redeSocial.adicionar_usuario(2, "Lucas")
    redeSocial.adicionar_usuario(3, "Alex")
    redeSocial.adicionar_usuario(4, "Amanda")
    redeSocial.adicionar_usuario(5, "Jose")
    redeSocial.adicionar_usuario(6, "Maria")
    redeSocial.adicionar_usuario(7, "Carla")

    print("Estabelecendo relacionamentos...")
    redeSocial.adicionar_relacionamento(1, 2)
    redeSocial.adicionar_relacionamento(1, 3)
    redeSocial.adicionar_relacionamento(4, 3)
    # redeSocial.adicionar_relacionamento(5, 6)
    redeSocial.adicionar_relacionamento(6, 7)

    redeSocial.mostrar_arvore()

    # redeSocial.remover_usuario(2)

    # usuario = redeSocial.encontrar_usuario(1)

    # if usuario:
    #     print(f"Usuário encontrado: {usuario.nome} ({
    #         usuario.usuario_id}) -> {[amigo.nome for amigo in usuario.relacionamentos]}")

    comunidades = redeSocial.encontrar_comunidades()

    for i, comunidade in enumerate(comunidades):
        print(f"Comunidade {
              i + 1}: {[usuario.nome for usuario in comunidade]}")


if __name__ == "__main__":
    main()
