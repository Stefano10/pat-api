#users.py

import os
import uuid
import mimetypes
import MySQLdb
import json
import collections
import falcon
import sys

from model.user import UserModel

# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.

class Users(object):
	def on_get(self, req, resp):
		#"""GET"""
		db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "processodesoftware")
		cursor = db.cursor()
		resp.status = falcon.HTTP_200  # Ok!
		#Executa a query
		cursor.execute("SELECT id, nome, email, idade FROM users")
		#Recebe todos os resultados
		query = cursor.fetchall()
		#Cria uma lista guardar os dados convertidos
		queryObjects = []
		#Converte
		for q in query:
				user = UserModel(q[0], q[1], q[2], q[3])
				queryObjects.append(user.__dict__)
		resp.body = json.dumps(queryObjects)
		db.close()

class User(object):
	def on_get(self, req, resp, id):
		#"""GET"""
		db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "processodesoftware")
		cursor = db.cursor()
		resp.status = falcon.HTTP_200  # Ok!
		id = int(id)
		#Executa a query
		sql = "SELECT id, nome, email, idade FROM users WHERE id = %d" % (id)
		cursor.execute(sql)
		#Recebe todos os resultados
		query = cursor.fetchall()
		#Cria uma lista guardar os dados convertidos
		queryObjects = []
		#Converte
		for q in query:
				user = UserModel(q[0], q[1], q[2], q[3])
				queryObjects.append(user.__dict__)
		resp.body = json.dumps(queryObjects)
		db.close()
		
	def on_post(self, req, resp):
		db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "processodesoftware")
		cursor = db.cursor()
		body = req.stream.read()
		newusersql = self.mountUser(body)
		equery = "INSERT INTO users (nome, email, idade, senha) VALUES (%s, %s, %s, %s)"

		try:
			cursor.execute(equery, (newusersql['name'], newusersql['email'], newusersql['age'], newusersql['password'],))
			cursor.execute("SELECT LAST_INSERT_ID() FROM users");
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
		db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "processodesoftware")
		cursor = db.cursor()
		#Recebe o id
		userid = id
		#forma a query
		equery = "DELETE FROM users WHERE id = %s" % (userid)
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

	def mountUser(self, uData):
		return json.loads(uData)

class UserEmail(object):
	def on_get(self, req, resp, email):
		#"""GET"""
		db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "processodesoftware")
		cursor = db.cursor()
		resp.status = falcon.HTTP_200  # Ok!
		#Executa a query
		sql = "SELECT id, nome, email, idade FROM users WHERE email LIKE '%s'" % (email)
		cursor.execute(sql)
		#Recebe todos os resultados
		query = cursor.fetchall()
		#Cria uma lista guardar os dados convertidos
		queryObjects = []
		#Converte
		for q in query:
				user = UserModel(q[0], q[1], q[2], q[3])
				queryObjects.append(user.__dict__)
		resp.body = json.dumps(queryObjects)
		db.close()      

class Login(object):
	def on_get(self, req, resp):
		#"""GET"""
		db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "processodesoftware")
		cursor = db.cursor()
		resp.status = falcon.HTTP_200  # Ok!
		#Executa a query

		body = req.stream.read()
		user = self.mountUser(body)

		sql = "SELECT true FROM users WHERE email = '%s' and senha = '%s'" % (user['email'], user['password'])
		cursor.execute(sql)
		#conta os resultados
		rows = cursor.rowcount

		result = {'logged' : True}
		
		if(rows <= 0):
			resp.status = falcon.HTTP_403
			result = {'logged' : False}

		resp.body = json.dumps(result)

		db.close()  

	def mountUser(self, uData):
		return json.loads(uData)