from Relacionamento import Relacionamento
import os


def mensagem_de_espera():
    input("Pressione enter para continuar...")
    # garante terminal limpo em qualquer SO
    os.system("cls" if os.name == "nt" else "clear")


def exibir_menu():
    print("\n===== [MENU] =====")
    print("1. Inserir usuário")
    print("2. Remover usuário")
    print("3. Visualizar Relacionamento(s)")
    print("4. Adicionar Relacionamento")
    print("5. Encontrar Usuário")
    print("6. Visualizar Comunidade(s)")
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
            mensagem_de_espera()

        elif escolha == '2':
            usuario_id = input("Digite o ID do usuário a ser removido: ")
            redeSocial.remover_usuario(usuario_id)
            print("")
            mensagem_de_espera()

        elif escolha == '3':
            print("Estrutura de relacionamentos:")
            redeSocial.mostrar_arvore()
            print("")
            mensagem_de_espera()

        elif escolha == '4':
            usuario_id1 = input("Digite o ID do primeiro usuário: ")
            usuario_id2 = input("Digite o ID do segundo usuário: ")
            redeSocial.adicionar_relacionamento(usuario_id1, usuario_id2)
            mensagem_de_espera()

        elif escolha == '5':
            usuario_id = input("Digite o ID do usuário a ser encontrado: ")
            usuario = redeSocial.encontrar_usuario(usuario_id)
            if usuario:
                print(f"Usuário encontrado: {usuario.nome} ({usuario.usuario_id})")  # nopep8
            print("")
            mensagem_de_espera()

        elif escolha == '6':
            comunidades = redeSocial.encontrar_comunidades()

            for idx, comunidade in enumerate(comunidades):
                print(f"Comunidade {idx + 1}:")

                for usuario in comunidade:
                    print(f"{usuario.nome} ({usuario.usuario_id})")

            print("")
            mensagem_de_espera()

        elif escolha == '0':
            print("Saindo...")
            break

        else:
            print("Opção incorreta. Por favor, escolha novamente.")
            mensagem_de_espera()


if __name__ == "__main__":
    main()
