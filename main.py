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

# things will handle all requests to the '/things' URL path
app.add_route('/pat/usuarios', Usuarios())
app.add_route('/pat/usuario', Usuario())
app.add_route('/pat/usuario/{id}', Usuario())
app.add_route('/pat/usuario/email/{email}', UsuarioEmail())
app.add_route('/pat/login', Login())

app.add_route('/pat/objetos', Objetos())
app.add_route('/pat/objeto', Objeto())
app.add_route('/pat/objeto/{id}', Objeto())
app.add_route('/pat/objeto/tombo/{id}', ObjetoTombo())
app.add_route('/pat/objeto/serial/{id}', ObjetoSerial())

#FALTA IMAGEM

#FALTA CAUTELA

#FALTA PROTOCOLO


