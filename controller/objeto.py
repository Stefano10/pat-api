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
					queryObjects.append(objeto.__dict__)
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
					queryObjects.append(objeto.__dict__)
			#Retorna a resposta
			resp.status = falcon.HTTP_200  # Ok!
			resp.body = json.dumps(queryObjects)
		except:
			print "GET ERROR: ", sys.exc_info()
			resp.status = falcon.HTTP_500
			resp.body = "Erro ao executar o acesso."
		db.close()

	def on_post(self, req, resp):



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
					queryObjects.append(objeto.__dict__)
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
					queryObjects.append(objeto.__dict__)
			#Retorna a resposta
			resp.status = falcon.HTTP_200  # Ok!
			resp.body = json.dumps(queryObjects)
		except:
			print "GET ERROR: ", sys.exc_info()
			resp.status = falcon.HTTP_500
			resp.body = "Erro ao executar o acesso."
		db.close()