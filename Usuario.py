class Usuario:
    def __init__(self, usuario_id, nome):
        self.usuario_id = usuario_id
        self.nome = nome
        self.relacionamentos = []

    def __repr__(self):
        return f"Usuario({self.usuario_id}, {self.nome})"
