#users.py

import os
import uuid
import mimetypes
import MySQLdb
import json
import collections
import falcon
import sys

from model.user_info import UserInfoModel

# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.

class UsersInfo(object):
	def on_get(self, req, resp):
		#"""GET"""
		db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "processodesoftware")
		cursor = db.cursor()
		resp.status = falcon.HTTP_200  # Ok!
		#Executa a query
		cursor.execute("SELECT id, facebook, whatsapp, id_user FROM users_info")
		#Recebe todos os resultados
		query = cursor.fetchall()
		#Cria uma lista guardar os dados convertidos
		queryObjects = []
		#Converte
		for q in query:
				user = UserInfoModel(q[0], q[1], q[2], q[3])
				queryObjects.append(user.__dict__)
		resp.body = json.dumps(queryObjects)
		db.close()

class UserInfo(object):
	def on_get(self, req, resp, id):
		#"""GET"""
		db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "processodesoftware")
		cursor = db.cursor()
		resp.status = falcon.HTTP_200  # Ok!
		id = int(id)
		#Executa a query
		sql = "SELECT id, facebook, whatsapp, id_user FROM users_info WHERE id_user = %d" % (id)
		cursor.execute(sql)
		#Recebe todos os resultados
		query = cursor.fetchall()
		#Cria uma lista guardar os dados convertidos
		queryObjects = []
		#Converte
		for q in query:
				user = UserInfoModel(q[0], q[1], q[2], q[3])
				queryObjects.append(user.__dict__)
		resp.body = json.dumps(queryObjects)
		db.close()

	def on_delete(self, req, resp, id):
		#cria a conexAo e o cursor
		db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "processodesoftware")
		cursor = db.cursor()
		#Recebe o id
		userid = id
		#forma a query
		equery = "DELETE FROM users_info WHERE id_user = %s" % (userid)
		#Executa
		try:
			cursor.execute(equery)
			db.commit()
			resp.status = falcon.HTTP_200
		except:
			db.rollback()
			print "Insert ERROR: ", sys.exc_info()[0]
			resp.status = falcon.HTTP_500
		db.close()

	def on_put(self, req, resp):
		#Ainda nao funciona.
		db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "processodesoftware")
		cursor = db.cursor()
		#Recebe o id do usuario
		resp.status = falcon.HTTP_200
		body = req.stream.read()
		newusersql = self.mountUserInfo(body)
		equery = "UPDATE users_info SET facebook = %s, whatsapp = %s WHERE id_user = %s"

		try:
			cursor.execute(equery, (newusersql['facebook'], newusersql['whatsapp'], newusersql['id_user'],))
			db.commit()
		except:
			db.rollback()
			print "Update ERROR: ", sys.exc_info()[0]
			resp.status = falcon.HTTP_500

		resp.body = body
		db.close()

	def on_post(self, req, resp):
		#cria a conexao e o cursor
		db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "processodesoftware")
		cursor = db.cursor()
		#Le os dados
		body = req.stream.read()
		newusersql = self.mountUserInfo(body)
		#Forma a query
		equery = "INSERT INTO users_info (facebook, whatsapp, id_user) VALUES (%s, %s, %s)"

		try:
			#executa a query e comita
			cursor.execute(equery, (newusersql['facebook'], newusersql['whatsapp'], newusersql['id_user'],))
			#recebe a id do novo user_info, e retorna o valor
			cursor.execute("SELECT LAST_INSERT_ID() FROM users_info")
			result = {'id': cursor.fetchone()[0]}
			resp.body = json.dumps(result)
			resp.status = falcon.HTTP_201
			db.commit()
		except:
			db.rollback()
			print "iNSERT ERROR: ", sys.exc_info()[0]
			resp.status = falcon.HTTP_500
			resp.body = "Erro ao alterar o banco de dados! As informacoes do usuario nao foram inseridas."
		db.close()

	def mountUserInfo(self, uData):
		return json.loads(uData)

