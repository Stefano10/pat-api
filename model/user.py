#user.py

class UserModel(object):
    
    def __init__(self, id, name, email, age, password=""):
        self.id = id
        self.name = name
        self.email = email
        self.age = age
        self.password = password
