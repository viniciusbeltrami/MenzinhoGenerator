class Estagiario:
    def __init__(self,nome,apelido):
        self.nome = nome
        self.apelido = apelido
        pass
    def __repr__(self):
        return f"Estagiario(nome={self.nome}, apelido={self.apelido})"