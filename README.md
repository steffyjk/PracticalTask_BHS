# PracticalTask_BHS


## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/steffyjk/PracticalTask_BHS.git
$ cd PracticalTask_BHS
```

Create a virtual environment to install dependencies in and activate it: [ For Windows System]

```sh
$ python -m venv env_name
$ .\env_name\Scripts\activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Create .env file & set the variable values

```sh
DB_NAME=db_name
DB_USER=postgres [ default ]
DB_PASSWORD=postgres [ default ]
DB_HOST=127.0.0.1 [ default ]
DB_PORT=5432 [ default ]
DEBUG=True [ default ]
```
To run the Project
```sh
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.
