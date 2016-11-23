# About the project

The project is a platform in which the users will be able to exchange knowledge through it. You can learn from playing the guitar to the basics of a programming language, in which there will be a knowledge exchange, meaning that since you will be teaching someone else, it is expected that you too will be learning from your study partner.

This platform is being developed by all participants in the Processos de Software course at UFRN.

# API Component

This component is responsible for create an API for use in web and android versions of system being developed.

## Technologies
- Python 3
- Falcon
- MySQL

## API Description
Api in development for the platform described above, includes the following methods: 

|   URL             | VERB   | BODY    | EXAMPLE | RESULT              |
| ---               |  ---   |  ---    | ---     | ---                 |
| /user             | POST   | JSON    | {<br/>"name":"Example",<br/>"email":"example@example.com",<br/>"age":"21",<br/>"password":"123456"<br/>} |   Add a user |
| /user/{id}        | GET    | empty   | ---     |   Return a user by given id |
| /user/{id}/skills  | GET    | empty   | ---     |   Return all skills of user = id |
| /user/{id}/interests  | GET    | empty   | ---     |   Return all interests of user = id |
| /user/email/{e-mail}    | GET    | empty   | --- |   Return a user by given email    |
| /user/{id}        | DELETE | empty   | ---     |   Delete user by id |
| /users            | GET    | empty   | ---     |   Return all users    |
| /users/skills      | GET    | empty   | ---     |   Return all pair user-skill |
| /users/skills      | POST    | JSON   |  {<br/> "id_user":"1", <br/>"id_skill":"2"<br/>}    |   Add a User-Skill relation |
| /users/interests     | GET    | empty   | ---     |   Return all pair user-interest |
| /users/interests      | POST    | JSON   |  {<br/> "id_user":"1", <br/>"id_skill":"2"<br/>}    |   Add a User-Interest relation |
| /login            | GET    | JSON   | {<br/>"email":"example@example.com",<br/>"password":"123456"<br/>}     |   Return a JSON with "logged" (if false something the user is not logged and if true the user is logged) |
| /infos      		| GET    | empty   | ---     |   Return all users information  | 
| /info/{id_user}   | GET    | empty   | ---     |   Return an specific user information | 
| /info/{id_user}   | DELETE    | empty   | ---     |   Delete user info by an user id | 
| /info   			| POST    | JSON   | {"facebook": "http://www.facebook.com/example", "whatsapp": "84111111111", "id_user": "5"}     |   Insert user information by an user id |
| /info   			| PUT    | JSON   | {"facebook": "http://www.facebook.com/example", "whatsapp": "84111111111", "id_user": "5"}     |   Update user information by an user id |
| /picture/{id_user}| GET    | empty   | ---     |   Return an url in format '/uploaded_pictures/filename.type' you might add server url before |
| /picture 			| POST   | JSON   | {<br/>"type": "imagetype (png OR jpg OR gif)", <br/>"bytecode": "imagebase64bytecode", <br/>"id_user": 1<br/>}     |   Upload an image on server to a given user |
| /skill/        | GET    | empty   | ---     |   Return all skills | 
| /skill/{id}        | GET    | empty   | ---     |   Return a skill by given id | 
| /skill/{id}/users  | GET    | empty   | ---     |   Return all users that has skill id  |
| /interest/{id}        | GET    | empty   | ---     |   Return a interest by given id | 
| /interest/{id}/users  | GET    | empty   | ---     |   Return all users that has interest id  | 




## Getting Started
### Installing prerequisites
To use the api server you will need Python 3, Falcon and a WSGI Server (in our project we use gunicorn).

To run our api server you will need to do this following steps one time:

1. Install python-pip and mysql-server if you don't have it;
2. Install the mysql client lib if you don't have it: `sudo apt-get install libmysqlclient-dev`;
3. Install python mysql lib: `# pip install MySQL-python`;
4. Install falcon using pip: `# pip install falcon`;
5. Install gunicorn using pip: `# pip install gevent gunicorn`.

For easier management of pip packages, it's recommended to use [virtualenv](https://virtualenv.pypa.io/en/stable/). It creates isolated Python environments, and does not need superuser privileges to install packages. 

### Running
To run the api server do the following: 

1. Clone the project: `$ git clone git@github.com:Processos-de-software-2016-2/python-api.git`;
2. Run the server: `gunicorn main:app --bind 0.0.0.0:<desired_port>`;
3. Make a HTTP request on port 8000 to any of the URLs listed in API Description section.

# How to Contribute
1. Clone the project: `$ git clone git@github.com:Processos-de-software-2016-2/python-api.git`;
2. If you already have the project update it: `$ git pull origin master`;
3. Create a branch to start coding: `$ git checkout -b <branch_name>`;
4. Commit and push your changes: `$ git push origin <branch_name>`;
5. Create a pull request from your branch to master.

# Team
- [Daniel Tiago de Souza Brito](https://github.com/danielmanfred)
- [João Eduardo Medeiros](https://github.com/joaomedeiros95)
- [Stefano Momo Loss](https://github.com/Stefano10)
- [Victor Santiago Valente](https://github.com/victorsv)
- [Vinícius Kleiton da Trindade Ramos](https://github.com/Vinnykt)

# Other Parts of this Project 

- [Android](https://github.com/Processos-de-software-2016-2/Android)
- [Infrastructure](https://github.com/Processos-de-software-2016-2/Infraestrutura) 
- [WebApp](https://github.com/Processos-de-software-2016-2/Web-App)
- [UX](https://github.com/Processos-de-software-2016-2/UX)
