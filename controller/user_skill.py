import os
import uuid
import mimetypes
import MySQLdb
import json
import collections
import falcon
import sys

from model.user_skill import UserSkillModel
from model.skill import SkillModel
from model.user import UserModel


# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.

class UserSkill(object):
    def on_get(self, req, resp):
        #"""GET ALL PAIR USER-SKILL"""
        db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "processodesoftware")
        cursor = db.cursor()
        resp.status = falcon.HTTP_200  # Ok!
        #Executa a query
        cursor.execute("SELECT  id , id_user, id_skill  FROM user_skills")
        #Recebe todos os resultados
        query = cursor.fetchall()
        #Cria uma lista guardar os dados convertidos
        queryObjects = []
        #Converte
        for q in query:
                user_skill = UserSkillModel(q[0], q[1], q[2])
                queryObjects.append(user_skill.__dict__)
        resp.body = json.dumps(queryObjects)
        db.close()

    def on_post(self, req, resp):
        db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "processodesoftware")
        cursor = db.cursor()
        body = req.stream.read()
        newusersql = self.mountUserSkill(body)
        equery = "INSERT INTO user_skills (id_user, id_skill) VALUES (%s, %s)"

        try:
            cursor.execute(equery, (newusersql['id_user'], newusersql['id_skill'],))
            cursor.execute("SELECT LAST_INSERT_ID() FROM user_skills");
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

    def mountUserSkill(self, uData):
        return json.loads(uData)

class UserSkill_Skill(object):
    def on_get(self, req, resp, id):
        #"""GET ALL USERS  WHO HAVE A SKILL ""
        db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "processodesoftware")
        cursor = db.cursor()
        resp.status = falcon.HTTP_200  # Ok!
        id = int(id)
        #Executa a query
        sql = "SELECT id_user FROM user_skills WHERE id_skill = %s" % (id)
        cursor.execute(sql)
        #Recebe todos os resultados
        query = cursor.fetchall()
        #Cria uma lista guardar os dados convertidos
        queryObjects = []
        #Converte
        for q in query:

                    id = int(q[0])
                    #Executa a query
                    sql = "SELECT id, nome, email, idade FROM users WHERE id = %d" % (id)
                    cursor.execute(sql)
                    #Recebe todos os resultados
                    query = cursor.fetchall()
                    #Converte
                    user = UserModel(query[0][0], query[0][1], query[0][2], query[0][3])
                    queryObjects.append(user.__dict__)

        resp.body = json.dumps(queryObjects)
        db.close()

class UserSkill_User(object):
    def on_get(self, req, resp, id):
        #"""GET ALL SKILLS  OF A  USER"
        db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "processodesoftware")
        cursor = db.cursor()
        resp.status = falcon.HTTP_200  # Ok!
        id = int(id)
        #Executa a query
        sql = "SELECT id_skill FROM user_skills WHERE id_user = %d" % (id)
        cursor.execute(sql)
        #Recebe todos os resultados
        query = cursor.fetchall()
        #Cria uma lista guardar os dados convertidos
        queryObjects = []
        #Converte
        for q in query:

                id = int(q[0])
                #Executa a query
                sql = "SELECT id, name FROM skills WHERE id = %d" % (id)
                cursor.execute(sql)
                #Recebe todos os resultados
                query = cursor.fetchall()
                #Cria uma lista guardar os dados convertidos
                skill = SkillModel(query[0][0], query[0][1])
                queryObjects.append(skill.__dict__)

        resp.body = json.dumps(queryObjects)
        db.close()