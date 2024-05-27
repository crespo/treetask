from Relacionamento import Relacionamento


def main():

    redeSocial = Relacionamento()
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
