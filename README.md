# Django-React-CRUD-API

- Creating react app
```bash
cd clint
yarn create vite app
cd app
yarn
```
- start the frontend
```bash
yarn dev
```

- creating django app
```bash
cd server
python3 -m venv .venv
source .venv/bin/activate
pip install django djangorestframework
pip list
django-admin startproject backend .
```
- start the backend
```bash
python3 manage.py runserver
```
- creating django app `api`
```bash
python3 manage.py startapp api
```
- make migrations
```bash
python3 manage.py makemigrations
```
- migrate
```bash
python3 manage.py migrate
```
