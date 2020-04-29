# FLASK USER AUTH WITH JSON WEB TOKEN

## Install dependencies

`pip install -r requirements.txt`

## To run tests

`pytest`

## To run API [Ubuntu]

`export FLASK_APP=flask_app`

`flask run`

## ENDPOINTS

### Homepage

- endpoint: '/'
- method: GET

NOTE: auth_token should be in header. "Bearer +auth_token"

### Signup

- endpoint: '/signup'
- method: POST
- data: { "email":"xxxxxx", "password":"xxxxxx"}

### Login

- endpoint: '/login'
- method: POST
- data: { "email":"xxxxxx", "password":"xxxxxx"}
