import unittest
import json

from aux import Aux

class FunTest(unittest.TestCase):

    aux = Aux()
    urlbase = "http://127.0.0.1:8000"

    def testPost(self):
        email = "apiteste1@teste.com"

        self.deleteUser(email)

        url= "/user"
        param = { "name":"Teste1","email":email,"age":"21","password":"123456"}
        self.assertEqual(self.aux.postFunction(self.urlbase, url, param), 201)

        self.deleteUser(email)

    def testGetByEmail(self):
        email = "apiteste2@teste.com"

        self.deleteUser(email)

        url= "/user"
        param = { "name":"Teste","email":email,"age":"21","password":"123456"}
        self.aux.postFunction(self.urlbase, url, param)
        url = "/user/email/" + email
        res = self.aux.getFunction(self.urlbase, url)
        self.assertEqual(json.loads(res)[0]['email'], email)

        self.deleteUser(email)

    def testDelete(self):
        email = "apiteste3@teste.com"

        self.deleteUser(email)

        url= "/user"
        param = { "name":"Teste3","email":email,"age":"21","password":"123456"}
        self.aux.postFunction(self.urlbase, url, param)

        url = "/user/email/" + email
        res = self.aux.getFunction(self.urlbase, url)
        idd = json.loads(res)[0]['id']
        url = "/user/"
        self.assertEqual( self.aux.deleteFunction(self.urlbase, url,idd), 200)

    def deleteUser(self, email):
        url = "/user/email/" + email
        res = self.aux.getFunction(self.urlbase, url)

        if res == "[]":
            return
            
        idd = json.loads(res)[0]['id']

        url = "/user/"
        self.aux.deleteFunction(self.urlbase, url,idd)



if __name__ == '__main__':
        unittest.main()
