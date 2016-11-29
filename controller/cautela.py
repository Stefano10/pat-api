import os
import uuid
import mimetypes
import MySQLdb
import json
import collections
import falcon
import sys

from model.objeto import ObjetoModel
from model.cautela import CautelaModel
from model.usuario import UsuarioModel


# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.

class cautela(object):
    def on_get(self, req, resp):

        db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "dbpat")
        cursor = db.cursor()
        resp.status = falcon.HTTP_200  # Ok!
        #Executa a query
        cursor.execute("SELECT  idUsuario, data_inicio, data_final, IdCautela, cautelado FROM cautela")
        #Recebe todos os resultados
        query = cursor.fetchall()
        #Cria uma lista guardar os dados convertidos
        queryObjects = []
        #Converte
        for q in query:
                cautela = CautelaModel(q[0], q[1], q[2], q[3], q[4])
                queryObjects.append(cautela.__dict__)
        resp.body = json.dumps(queryObjects)
        db.close()

    def on_post(self, req, resp):
        db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "dbpat")
        cursor = db.cursor()
        body = req.stream.read()
        newusersql = self.mountCautela(body)
        equery = "INSERT INTO cautela (idUsuario, data_inicio, data_final, cautelado) VALUES (%s, %s, %s, %s, %s)"

        try:
            cursor.execute(equery, (newusersql['idUsuario'], newusersql['data_inicio'],newusersql['data_final'], newusersql['cautelado'], ))
            cursor.execute("SELECT LAST_INSERT_ID() FROM cautela");
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

    def mountCautela(self, uData):
        return json.loads(uData)

class Cautela_Usuario(object):
    def on_get(self, req, resp, idUsuario):
        #GET EM TODAS CAUTELAS FEITAS POR UM USUARIO
        db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "dbpat")
        cursor = db.cursor()
        resp.status = falcon.HTTP_200  # Ok!
        id = int(id)
        #Executa a query
        sql = "SELECT idUsuario, data_inicio, data_final, IdCautela, cautelado FROM cautela WHERE idUsuario = %s" % (idUsuario)
        cursor.execute(sql)
        #Recebe todos os resultados
        query = cursor.fetchall()
        #Cria uma lista guardar os dados convertidos
        queryObjects = []
        #Converte
        for q in query:
                    cautela = CautelaModel(q[0], q[1], q[2], q[3], q[4])
                    queryObjects.append(cautela.__dict__)

        resp.body = json.dumps(queryObjects)
        db.close()

class Cautela_Cautelado(object):
    def on_get(self, req, resp, cautelado):
        #GET EM TODAS AS CAUTELAS DE UM CAUTELADO
        db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "dbpat")
        cursor = db.cursor()
        resp.status = falcon.HTTP_200  # Ok!
        id = int(id)
        #Executa a query
        sql = "SELECT  idUsuario, data_inicio, data_final, IdCautela, cautelado FROM cautela WHERE cautelado = %s" % (cautelado)
        cursor.execute(sql)
        #Recebe todos os resultados
        query = cursor.fetchall()
        #Cria uma lista guardar os dados convertidos
        queryObjects = []
        #Converte
        for q in query:
                    cautela = CautelaModel(q[0], q[1], q[2], q[3], q[4])
                    queryObjects.append(cautela.__dict__)

        resp.body = json.dumps(queryObjects)
        db.close()