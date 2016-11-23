import requests

import json

class Aux:
    def getFunction(self,urlbase, url):
        response = requests.get(urlbase+url)

        if response.status_code != 200:
                raise Exception("Error at function GET - Code: "+ str(response.status_code))
        return response.content

    def postFunction(self,urlbase, url, param):
        headers = {'content-type': 'application/json'}
        response = requests.post(urlbase+url, data=json.dumps(param), headers=headers)
        if response.status_code != 201:
               raise Exception("Error at function POST - Code: "+ str(response.status_code))
        return response.status_code

    def deleteFunction(self,urlbase, url,idd):
    	response = requests.delete(urlbase+url+str(idd))
    	if response.status_code != 200:
    		raise Exception("Error at function DELETE - Code: "+ str(response.status_code))
    	return response.status_code

    def putFunction(self,urlbase, url, param):
        response = requests.put(urlbase+url, json=param)
        if response.status_code != 200:
                raise Exception("Error at function PUT - Code: "+ str(response.status_code))
        return response

    if __name__ == "__main__":
        print ("MAIN")
