#user.py

class CautelaModel(object):

    def __init__(self, idUsuario, data_inicio, data_final, IdCautela, cautelado , idObjeto):
        self.idUsuario = idUsuario
        self.data_inicio = data_inicio
        self.data_final = data_final
        self.IdCautela = IdCautela
        self.cautelado=cautelado
        self.idObjeto = idObjeto
