#users.py

import os
import uuid
import mimetypes
import MySQLdb
import json
import collections
import falcon
import sys
import base64

from model.user_info import UserInfoModel

# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.

class Images(object):
	url = "/uploaded_pictures/"
	path = "/var/www/html/uploaded_pictures/"

	def on_post(self, req, resp):
		db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "processodesoftware")
		cursor = db.cursor()
		body = req.stream.read()
		image = self.mountImage(body)

		filename = uuid.uuid4().urn[9:] + "." + image['type']
		bytecode = image['bytecode']
		userid = image['id_user']

		try:
			fh = open(self.path + filename, "wb")
			fh.write(base64.b64decode(bytecode))	
			fh.close()

			equery = "INSERT INTO pictures (filename, id_user) VALUES ('%s', %s)" % (filename, userid)
			cursor.execute(equery)

			resp.body = json.dumps({"filename": filename})
			resp.status = falcon.HTTP_201 

			db.commit()
		except:
			db.rollback()
			resp.status = falcon.HTTP_500
			resp.body = "Ocorreu um erro"
			print "Insert ERROR: ", sys.exc_info()

		db.close()

	def on_get(self, req, resp, id):
		db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "processodesoftware")
		cursor = db.cursor()
		userid = id

		try:
			equery = "SELECT filename FROM pictures WHERE id_user = %s ORDER BY id DESC LIMIT 1" % (userid)
			cursor.execute(equery)
			filename = self.url + cursor.fetchone()[0]

			resp.body = json.dumps({"url": filename})
			resp.status = falcon.HTTP_200

			db.commit()
		except:
			db.rollback()
			resp.status = falcon.HTTP_500
			resp.body = "Ocorreu um erro"
			print "GET ERROR: ", sys.exc_info()

		db.close()

	def mountImage(self, uData):
		return json.loads(uData)
