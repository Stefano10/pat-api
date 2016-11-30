# main.py

import os
import uuid
import mimetypes
import falcon
import gevent
from gevent import socket
from controller.usuarios import *
from controller.protocolo import *
from controller.imagem import *
from controller.objeto import *
from controller.cautela import *

# falcon.API instances are callable WSGI apps
app = falcon.API()

#USUARIOS
app.add_route('/pat/usuarios', Usuarios())
app.add_route('/pat/usuario', Usuario())
app.add_route('/pat/usuario/{id}', Usuario())
app.add_route('/pat/usuario/email/{email}', UsuarioEmail())
app.add_route('/pat/login', Login())

#OBJETOS
app.add_route('/pat/objetos', Objetos())
app.add_route('/pat/objeto', Objeto())
app.add_route('/pat/objeto/{id}', Objeto())
app.add_route('/pat/objeto/tombo/{id}', ObjetoTombo())
app.add_route('/pat/objeto/serial/{id}', ObjetoSerial())

#IMAGEM
app.add_route('/pat/imagem', Imagem())
app.add_route('/pat/imagem/{id}', Imagem())

#CAUTELA
app.add_route('/pat/cautelas', Cautelas())
app.add_route('/pat/cautela', Cautela())
app.add_route('/pat/cautela/{id}', Cautela())
app.add_route('/pat/cautela/usuario/{id}', Cautela_Usuario())
app.add_route('/pat/cautela/cautelado/{id}', Cautela_Cautelado())
app.add_route('/pat/cautela/objeto/{id}', Cautela_Objeto())

#PROTOCOLO
app.add_route('/pat/protocolos', Protocolos())
app.add_route('/pat/protocolo', Protocolo())
app.add_route('/pat/protocolo/{id}', Protocolo())
app.add_route('/pat/protocolo/objeto/{id}', Protocolo_Objeto())
app.add_route('/pat/protocolo/usuario/{id}', Protocolo_Usuario())



