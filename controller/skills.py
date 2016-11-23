#skills.py

import os
import uuid
import mimetypes
import MySQLdb
import json
import collections
import falcon
import sys

from model.skill import SkillModel

# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.

class Skills(object):
	def on_get(self, req, resp):
		#Retorna todas as skills presentes no banco de dados.
		db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "processodesoftware")
		cursor = db.cursor()
		try:
			#Executa a query
			cursor.execute("SELECT id, name FROM skills")
			#Recebe todos os resultados
			query = cursor.fetchall()
			#Cria uma lista guardar os dados convertidos
			queryObjects = []
			#Converte
			for q in query:
					skill = SkillModel(q[0], q[1])
					queryObjects.append(skill.__dict__)
			#Retorna a resposta
			resp.status = falcon.HTTP_200  # Ok!
			resp.body = json.dumps(queryObjects)
		except:
			print "GET ERROR: ", sys.exc_info()
			resp.status = falcon.HTTP_500
			resp.body = "Erro ao executar o acesso."
		db.close()

class Skill(object):
	def on_get(self, req, resp, id):
		#Retorna apenas uma skill presentes no banco de dados.
		db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "processodesoftware")
		cursor = db.cursor()
		try:
			#Executa a query
			sql = "SELECT id, name FROM skills WHERE id = %s" % (id)
			cursor.execute(sql)
			#Recebe todos os resultados
			query = cursor.fetchall()
			#Cria uma lista guardar os dados convertidos
			queryObjects = []
			#Converte
			for q in query:
					skill = SkillModel(q[0], q[1])
					queryObjects.append(skill.__dict__)
			#Retorna a resposta
			resp.status = falcon.HTTP_200  # Ok!
			resp.body = json.dumps(queryObjects)
		except:
			print "GET ERROR: ", sys.exc_info()
			resp.status = falcon.HTTP_500
			resp.body = "Erro ao executar o acesso."
		db.close()
