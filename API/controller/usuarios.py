#usuario.py

import os
import uuid
import mimetypes
import MySQLdb
import json
import collections
import falcon
import sys

from model.usuario import UsuarioModel

# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.

class Usuarios(object):
	def on_get(self, req, resp):
		#"""GET"""
		db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "dbpat")
		cursor = db.cursor()
		resp.status = falcon.HTTP_200  # Ok!
		#Executa a query
		cursor.execute("SELECT idUsuario, name, email, senha, nvacesso FROM usuario")
		#Recebe todos os resultados
		query = cursor.fetchall()
		#Cria uma lista guardar os dados convertidos
		queryObjects = []
		#Converte
		for q in query:
				user = UsuarioModel(q[0], q[1], q[2], q[3], q[4])
				queryObjects.append(user.__dict__)
		resp.body = json.dumps(queryObjects)
		db.close()

class Usuario(object):
	def on_get(self, req, resp, id):
		#"""GET"""
		db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "dbpat")
		cursor = db.cursor()
		resp.status = falcon.HTTP_200  # Ok!
		id = int(id)
		#Executa a query
		sql = "SELECT idUsuario, name, email, senha, nvacesso FROM usuario WHERE idUsuario = %d" % (idUsuario)
		cursor.execute(sql)
		#Recebe todos os resultados
		query = cursor.fetchall()
		#Cria uma lista guardar os dados convertidos
		queryObjects = []
		#Converte
		for q in query:
				user = UsuarioModel(q[0], q[1], q[2], q[3])
				queryObjects.append(user.__dict__)
		resp.body = json.dumps(queryObjects)
		db.close()

	def on_post(self, req, resp):
		db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "dbpat")
		cursor = db.cursor()
		body = req.stream.read()
		newusuarioql = self.mountUsuario(body)
		equery = "INSERT INTO usuario ( name, email, senha, nvacesso) VALUES (%s, %s, %s, %s)"

		try:
			cursor.execute(equery, (newusuarioql['name'], newusuarioql['email'], newusuarioql['senha'], newusuarioql['nvacesso'],))
			cursor.execute("SELECT LAST_INSERT_ID() FROM usuario");
			result = {'id': int(cursor.fetchone()[0])}
			resp.body = json.dumps(result)
			resp.status = falcon.HTTP_201
			db.commit()
		except:
			db.rollback()
			print "Insert ERROR: ", sys.exc_info()[0]
			resp.status = falcon.HTTP_500
			resp.body = "Erro ao alterar o banco de dados! Usuario nao foi inserido."
		db.close()

	def on_delete(self, req, resp, id):
		#cria a conexAo e o cursor
		db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "dbpat")
		cursor = db.cursor()
		#Recebe o id
		idUsuario = id
		#forma a query
		equery = "DELETE FROM usuario WHERE idUsuario = %s" % (idUsuario)
		#Executa
		try:
			cursor.execute(equery)
			db.commit()
			resp.status = falcon.HTTP_200
		except:
			db.rollback()
			print "Delete ERROR: ", sys.exc_info()
			resp.status = falcon.HTTP_500
		db.close()

	def mountUsuario(self, uData):
		return json.loads(uData)

class UsuarioEmail(object):
	def on_get(self, req, resp, email):
		#"""GET"""
		db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "dbpat")
		cursor = db.cursor()
		resp.status = falcon.HTTP_200  # Ok!
		#Executa a query
		sql = "SELECT idUsuario, name, email, senha, nvacesso FROM usuario WHERE email LIKE '%s'" % (email)
		cursor.execute(sql)
		#Recebe todos os resultados
		query = cursor.fetchall()
		#Cria uma lista guardar os dados convertidos
		queryObjects = []
		#Converte
		for q in query:
				user = UsuarioModel(q[0], q[1], q[2], q[3])
				queryObjects.append(user.__dict__)
		resp.body = json.dumps(queryObjects)
		db.close()

class Login(object):
	def on_post(self, req, resp):
		#"""GET"""
		db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "dbpat",charset="utf8", use_unicode = True)
		cursor = db.cursor()
		resp.status = falcon.HTTP_200  # Ok!
		#Executa a query

		body = req.stream.read()
		user = self.mountUsuario(body)

		sql = "SELECT true FROM usuario WHERE email = '%s' and senha = '%s'" % (user['email'], user['senha'])
		cursor.execute(sql)
		#conta os resultados
		rows = cursor.rowcount

		if(rows <= 0):
			resp.status = falcon.HTTP_403

		db.close()

	def mountUsuario(self, uData):
		return json.loads(uData)
