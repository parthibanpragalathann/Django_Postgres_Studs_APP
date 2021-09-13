# Student result application using Django with Postgresql

#### Create virtual environment and activated it.
#### whatever any IDE your wish like pycharm, vscode and sublime

## Requirements
- Python - 3 and above
- postgresql

## installation:
```python
$ pip install -r requirements.txt
```

## Database migration

```python
$ python manage.py makemigrations
$ python manage.py migrate
```

## Run server
```python
$ python manage.py runserver
```

## Api's
#### Below api requests all using curl.

### Get student details

```bash
curl http://127.0.0.1:8000/api/student/
```

## Create student

curl -d '{"Name":"samir", "RollNumber":"21ds16", "DateofBirth": "2021-09-30"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8000/api/student/

/api/student/pk/marks/add/

### Add marks to particular student

```bash
curl -d '{"marks":87}' -H "Content-Type: application/json" -X PUT http://127.0.0.1:8000/api/student/pk/marks/add/
```


/api/student/pk/marks/

## Get particular student mark

```bash
curl http://127.0.0.1:8000/api/student/pk/marks/
```


/api/student/marks/

## Get all students marks 

```bash
curl http://127.0.0.1:8000/api/student/marks/
```


/api/student/results/

## Get students results

```bash
curl http://127.0.0.1:8000/api/student/results/
```

