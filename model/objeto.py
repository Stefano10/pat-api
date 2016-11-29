#user.py

class ObjetoModel(object):

    def __init__(self, id, tombo, serialn, local, descricao, situacao ):
        self.id = id
        self.tombo = tombo
        self.serialn = serialn
        self.local = local
        self.descricao=descricao
        self.situacao=situacao
