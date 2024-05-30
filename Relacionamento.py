from Usuario import Usuario


class Relacionamento:
    def __init__(self):
        self.usuarios = {}

    def adicionar_usuario(self, usuario_id, nome):
        if usuario_id in self.usuarios:
            print(f"Usuario {usuario_id} já existe.")
        elif self.naoEhInteiro(usuario_id):
            print("ID do usuário deve ser um valor do tipo inteiro")
        elif int(usuario_id) < 0:
            print("ID do usuário deve ser maior que zero")
        else:
            self.usuarios[usuario_id] = Usuario(usuario_id, nome)
            print(f"Usuário {usuario_id} adicionado com sucesso!")

    def adicionar_relacionamento(self, usuario_id1, usuario_id2):
        if not (usuario_id1 in self.usuarios) or not (usuario_id2 in self.usuarios):
            print(f"Um ou ambos usuários não achados: {usuario_id1}, {usuario_id2}")  # nopep8
        elif self.existeRelacionamentoEntre(usuario_id1, usuario_id2):
            print(f"Relacionamento entre {usuario_id1} e {usuario_id2} já existe")  # nopep8
        elif usuario_id1 == usuario_id2:
            print(f"Relacionamentos devem ser entre usuários diferentes")
        else:
            print(self.usuarios[usuario_id1].relacionamentos)
            self.usuarios[usuario_id1].relacionamentos.append(self.usuarios[usuario_id2])  # nopep8
            self.usuarios[usuario_id2].relacionamentos.append(self.usuarios[usuario_id1])  # nopep8
            print(f"Relacionamento entre {usuario_id1} e {usuario_id2} adicionado com sucesso!")  # nopep8

    def remover_usuario(self, usuario_id):
        if usuario_id in self.usuarios:
            for amigo in self.usuarios[usuario_id].relacionamentos:
                amigo.relacionamentos.remove(self.usuarios[usuario_id])
            del self.usuarios[usuario_id]
            print(f"Usuário {usuario_id} removido com sucesso!")
        else:
            print(f"Usuario {usuario_id} não encontrado.")

    def mostrar_arvore(self):
        for usuario in self.usuarios.values():
            print(f"{usuario.nome} ({usuario.usuario_id}) -> {[amigo.nome for amigo in usuario.relacionamentos]}")  # nopep8

    def encontrar_usuario(self, usuario_id):
        if usuario_id in self.usuarios:
            return self.usuarios[usuario_id]
        else:
            print(f"Usuario {usuario_id} não encontrado.")
            return None

    # Encontrar comunidades baseadas em relacionamentos
    def encontrar_comunidades(self):
        visitado = set()
        comunidades = []

        def dfs(usuario, comunidade):
            visitado.add(usuario.usuario_id)
            comunidade.append(usuario)
            for amigo in usuario.relacionamentos:
                if amigo.usuario_id not in visitado:
                    dfs(amigo, comunidade)

        for usuario in self.usuarios.values():
            if usuario.usuario_id not in visitado:
                comunidade = []
                dfs(usuario, comunidade)
                comunidades.append(comunidade)

        return comunidades

    def existeRelacionamentoEntre(self, usuario_id1, usuario_id2):
        for usuario in self.usuarios[usuario_id1].relacionamentos:
            if usuario.usuario_id == usuario_id2:
                return True

        return False

    def naoEhInteiro(self, s):
        try:
            int(s)
        except ValueError:
            return True
        else:
            return False
