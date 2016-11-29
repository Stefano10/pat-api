import os
import uuid
import mimetypes
import MySQLdb
import json
import collections
import falcon
import sys

from model.objeto import ObjetoModel
from model.protocolo import ProtocoloModel
from model.usuario import UsuarioModel


# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.

class Protocolo(object):
    def on_get(self, req, resp):

        db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "dbpat")
        cursor = db.cursor()
        resp.status = falcon.HTTP_200  # Ok!
        #Executa a query
        cursor.execute("SELECT  idProtocolo, origem, destino, idObjeto, data, idUsuario FROM protocolo")
        #Recebe todos os resultados
        query = cursor.fetchall()
        #Cria uma lista guardar os dados convertidos
        queryObjects = []
        #Converte
        for q in query:
                protocolo = ProtocoloModel(q[0], q[1], q[2], q[3], q[4], q[5])
                queryObjects.append(protocolo.__dict__)
        resp.body = json.dumps(queryObjects)
        db.close()

    def on_post(self, req, resp):
        db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "dbpat")
        cursor = db.cursor()
        body = req.stream.read()
        newusersql = self.mountProtocolo(body)
        equery = "INSERT INTO protocolo (origem, destino, idObjeto, data, idUsuario) VALUES (%s, %s, %s, %s, %s)"

        try:
            cursor.execute(equery, (newusersql['origem'], newusersql['destino'],newusersql['idObjeto'], newusersql['data'],newusersql['idUsuario'], ))
            cursor.execute("SELECT LAST_INSERT_ID() FROM protocolo");
            result = {'id': int(cursor.fetchone()[0])}
            resp.body = json.dumps(result)
            resp.status = falcon.HTTP_201
            db.commit()
        except:
            db.rollback()
            print "Insert ERROR: ", sys.exc_info()
            resp.status = falcon.HTTP_500
            resp.body = "Erro ao inserir Par: Usuario-Habilidade"
        db.close()

    def mountProtocolo(self, uData):
        return json.loads(uData)

class Protocolo_Objeto(object):
    def on_get(self, req, resp, idObjeto):
        #GET EM TODOS PROCOCOLOS DO OBJETO
        db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "dbpat")
        cursor = db.cursor()
        resp.status = falcon.HTTP_200  # Ok!
        id = int(id)
        #Executa a query
        sql = "SELECT  idProtocolo, origem, destino, idObjeto, data, idUsuario FROM protocolo WHERE idObjeto = %s" % (idObjeto)
        cursor.execute(sql)
        #Recebe todos os resultados
        query = cursor.fetchall()
        #Cria uma lista guardar os dados convertidos
        queryObjects = []
        #Converte
        for q in query:
                    protocolo = ProtocoloModel(q[0], q[1], q[2], q[3], q[4], q[5])
                    queryObjects.append(protocolo.__dict__)

        resp.body = json.dumps(queryObjects)
        db.close()

class Protocolo_Usuario(object):
    def on_get(self, req, resp, idUsuario):
        #GET EM TODOS PROCOCOLOS DO OBJETO
        db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "dbpat")
        cursor = db.cursor()
        resp.status = falcon.HTTP_200  # Ok!
        id = int(id)
        #Executa a query
        sql = "SELECT  idProtocolo, origem, destino, idObjeto, data, idUsuario FROM protocolo WHERE idUsuario = %s" % (idUsuario)
        cursor.execute(sql)
        #Recebe todos os resultados
        query = cursor.fetchall()
        #Cria uma lista guardar os dados convertidos
        queryObjects = []
        #Converte
        for q in query:
                    protocolo = ProtocoloModel(q[0], q[1], q[2], q[3], q[4], q[5])
                    queryObjects.append(protocolo.__dict__)

        resp.body = json.dumps(queryObjects)
        db.close()