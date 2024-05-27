from Usuario import Usuario


class Relacionamento:
    def __init__(self):
        self.usuarios = {}

    def adicionar_usuario(self, usuario_id, nome):
        if usuario_id not in self.usuarios:
            self.usuarios[usuario_id] = Usuario(usuario_id, nome)
        else:
            print(f"Usuario {usuario_id} já existe.")

    def adicionar_relacionamento(self, usuario_id1, usuario_id2):
        if usuario_id1 in self.usuarios and usuario_id2 in self.usuarios:
            self.usuarios[usuario_id1].relacionamentos.append(
                self.usuarios[usuario_id2])
            self.usuarios[usuario_id2].relacionamentos.append(
                self.usuarios[usuario_id1])
        else:
            print(f"Um ou ambos usuários não achados: {
                  usuario_id1}, {usuario_id2}")

    def remover_usuario(self, usuario_id):
        if usuario_id in self.usuarios:
            for amigo in self.usuarios[usuario_id].relacionamentos:
                amigo.relacionamentos.remove(self.usuarios[usuario_id])
            del self.usuarios[usuario_id]
        else:
            print(f"Usuario {usuario_id} não encontrado.")

    def mostrar_arvore(self):
        for usuario in self.usuarios.values():
            print(f"{usuario.nome} ({
                usuario.usuario_id}) -> {[amigo.nome for amigo in usuario.relacionamentos]}")

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
