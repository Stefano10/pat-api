#user.py

class ProtocoloModel(object):

    def __init__(self, idProtocolo, origem, destino, idObjeto, data, idUsuario):
        self.idProtocolo = idProtocolo
        self.origem = origem
        self.destino = destino
        self.idObjeto = idObjeto
        self.data=data
        self.idUsuario = idUsuario
