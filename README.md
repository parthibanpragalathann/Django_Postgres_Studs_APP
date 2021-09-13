#Student result application using Django with Postgresql


##installation:

###Create virtual environment and activated it.
###### whatever any IDE your wish like pycharm, vscode and sublime


####$sudo pip install -r requirements.txt

##Database migration

####$ python manage.py makemigrations
####$ python manage.py migrate
##Run server
####$ python manage.py runserver

##Using django with postgresql databases.

##Below api requsts all using curl.

###Get student details

####curl http://127.0.0.1:8000/api/student/

####Post student details

####curl -d '{"Name":"samir", "RollNumber":"21ds16", "DateofBirth": "2021-09-30"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8000/api/student/

###/api/student/pk/marks/add/

###Add marks to particular student

####curl -d '{"marks":87}' -H "Content-Type: application/json" -X PUT http://127.0.0.1:8000/api/student/pk/marks/add/

###/api/student/pk/marks/

##Get particular student mark

####curl http://127.0.0.1:8000/api/student/pk/marks/

###/api/student/marks/

####Get all students marks curl http://127.0.0.1:8000/api/student/marks/

###/api/student/results/

##Get student results

####curl http://127.0.0.1:8000/api/student/results/