class Bem:

    def __init__(self, patrimonio,descricao,local,verificado_por=None,status=None, verificado_em=None):
        self._patrimonio= patrimonio
        self._descricao = descricao
        self.local = local
        self.verificado_por= verificado_por
        self.status = status
        self.verificado_em= verificado_em

    @property
    def patrimonio(self):
        return self._patrimonio

    @property
    def descricao(self):
        return self._descricao

class Usuario:
    def __init__(self, id, nome, email, senha):
        self.id = id
        self.nome = nome
        self.email= email
        self.senha = senha


