from SocialNetworkTree import SocialNetworkTree


def main():
    # Inserindo usuários
    network = SocialNetworkTree()
    print("Inserindo 3 usuários...")
    network.add_user(1, "Alice")
    network.add_user(2, "Bob")
    network.add_user(3, "Charlie")

    # Estabelecendo relacionamentos
    print("Estabelecendo relacionamentos...")
    network.add_relationship(1, 2)
    network.add_relationship(1, 3)

    # Visualizando a árvore
    network.display_tree()

    # Removendo um usuário
    # print("Removendo usuário 2...")
    # network.remove_user(2)

    # Visualizando a árvore após remoção
    network.display_tree()

    # Buscando um usuário
    user = network.find_user(1)
    if user:
        print(f"User found: {user.name} ({
              user.user_id}) -> {[friend.name for friend in user.relationships]}")

    communities = network.find_communities()

    for idx, community in enumerate(communities):
        print(f"Community {idx + 1}: {[user.name for user in community]}")


if __name__ == "__main__":
    main()
