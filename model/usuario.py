#user.py

class UsuarioModel(object):

    def __init__(self, idUsuario, name, email, senha="****", nvacesso):
        self.idUsuario = idUsuario
        self.name = name
        self.email = email
        self.senha = senha
        self.nvacesso=nvacesso
