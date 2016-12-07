#objeto.py

import os
import uuid
import mimetypes
import MySQLdb
import json
import collections
import falcon
import sys

from model.objeto import ObjetoModel

# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.

class Objetos(object):
	def on_get(self, req, resp):
		#Retorna todas os objeto presentes no banco de dados.
		db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "dbpat")
		cursor = db.cursor()
		try:
			#Executa a query
			cursor.execute("SELECT id, tombo, serialn, local, descricao, situacao FROM objeto")
			#Recebe todos os resultados
			query = cursor.fetchall()
			#Cria uma lista guardar os dados convertidos
			queryObjects = []
			#Converte
			for q in query:
					obj = ObjetoModel(q[0], q[1], q[2], q[3],q[4], q[5])
					queryObjects.append(obj.__dict__)
			#Retorna a resposta
			resp.status = falcon.HTTP_200  # Ok!
			resp.body = json.dumps(queryObjects)
		except:
			print "GET ERROR: ", sys.exc_info()
			resp.status = falcon.HTTP_500
			resp.body = "Erro ao executar o acesso."
		db.close()



class Objeto(object):
	def on_get(self, req, resp, id):
		#Retorna apenas uma skill presentes no banco de dados.
		db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "dbpat")
		cursor = db.cursor()
		try:
			#Executa a query
			sql = "SELECT id, tombo, serialn, local, descricao, situacao FROM objeto WHERE id = %s" % (id)
			cursor.execute(sql)
			#Recebe todos os resultados
			query = cursor.fetchall()
			#Cria uma lista guardar os dados convertidos
			queryObjects = []
			#Converte
			for q in query:
					obj = ObjetoModel(q[0], q[1], q[2], q[3],q[4], q[5])
					queryObjects.append(obj.__dict__)
			#Retorna a resposta
			resp.status = falcon.HTTP_200  # Ok!
			resp.body = json.dumps(queryObjects)
		except:
			print "GET ERROR: ", sys.exc_info()
			resp.status = falcon.HTTP_500
			resp.body = "Erro ao executar o acesso."
		db.close()

    	def on_post(self, req, resp):
                        db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "dbpat")
                        cursor = db.cursor()
                        body = req.stream.read()
                        newusuarioql = self.mountObjeto(body)
                        equery = "INSERT INTO objeto ( tombo, serialn, local, descricao, situacao ) VALUES (%s, %s, %s, %s, %s)"

                        try:
                            cursor.execute(equery, (newusuarioql['tombo'], newusuarioql['serialn'], newusuarioql['local'], newusuarioql['descricao'],newusuarioql['situacao'],))
                            cursor.execute("SELECT LAST_INSERT_ID() FROM objeto");
                            result = {'id': int(cursor.fetchone()[0])}
                            resp.body = json.dumps(result)
                            resp.status = falcon.HTTP_201
                            db.commit()
                        except:
                            db.rollback()
                            print "Insert ERROR: ", sys.exc_info()[0]
                            resp.status = falcon.HTTP_500
                            resp.body = "Erro ao alterar o banco de dados! Objeto nao foi inserido."
                        db.close()

            def mountObjeto(self, uData):
		return json.loads(uData)

class ObjetoTombo(object):
	def on_get(self, req, resp, tombo):
		#Retorna apenas uma skill presentes no banco de dados.
		db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "dbpat")
		cursor = db.cursor()
		try:
			#Executa a query
			sql = "SELECT id, tombo, serialn, local, descricao, situacao FROM objeto WHERE tombo = %s" % (tombo)
			cursor.execute(sql)
			#Recebe todos os resultados
			query = cursor.fetchall()
			#Cria uma lista guardar os dados convertidos
			queryObjects = []
			#Converte
			for q in query:
					obj = ObjetoModel(q[0], q[1], q[2], q[3],q[4], q[5])
					queryObjects.append(obj.__dict__)
			#Retorna a resposta
			resp.status = falcon.HTTP_200  # Ok!
			resp.body = json.dumps(queryObjects)
		except:
			print "GET ERROR: ", sys.exc_info()
			resp.status = falcon.HTTP_500
			resp.body = "Erro ao executar o acesso."
		db.close()

class ObjetoSerial(object):
	def on_get(self, req, resp, serialn):
		#Retorna apenas uma skill presentes no banco de dados.
		db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "dbpat")
		cursor = db.cursor()
		try:
			#Executa a query
			sql = "SELECT id, tombo, serialn, local, descricao, situacao FROM objeto WHERE serialn = %s" % (serialn)
			cursor.execute(sql)
			#Recebe todos os resultados
			query = cursor.fetchall()
			#Cria uma lista guardar os dados convertidos
			queryObjects = []
			#Converte
			for q in query:
					obj = ObjetoModel(q[0], q[1], q[2], q[3],q[4], q[5])
					queryObjects.append(obj.__dict__)
			#Retorna a resposta
			resp.status = falcon.HTTP_200  # Ok!
			resp.body = json.dumps(queryObjects)
		except:
			print "GET ERROR: ", sys.exc_info()
			resp.status = falcon.HTTP_500
			resp.body = "Erro ao executar o acesso."
		db.close()

class ObjetoLocal(object):
	def on_get(self, req, resp, local):
		#Retorna apenas uma skill presentes no banco de dados.
		db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "dbpat")
		cursor = db.cursor()
		try:
			#Executa a query
			sql = "SELECT id, tombo, serialn, local, descricao, situacao FROM objeto WHERE local LIKE %s" % (local)
			cursor.execute(sql)
			#Recebe todos os resultados
			query = cursor.fetchall()
			#Cria uma lista guardar os dados convertidos
			queryObjects = []
			#Converte
			for q in query:
					obj = ObjetoModel(q[0], q[1], q[2], q[3],q[4], q[5])
					queryObjects.append(obj.__dict__)
			#Retorna a resposta
			resp.status = falcon.HTTP_200  # Ok!
			resp.body = json.dumps(queryObjects)
		except:
			print "GET ERROR: ", sys.exc_info()
			resp.status = falcon.HTTP_500
			resp.body = "Erro ao executar o acesso."
		db.close()