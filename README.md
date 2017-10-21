# TravelPlanProject
旅行計画ブラウザアプリ

## What is this?
Make travel plan application using Django Rest Framework and Angular 4

Authentication function is currently under development.

## Operating environment
- macOS Sierra 10.12.6
- python 3.6.1
- Django 1.11.4
- django-cors-headers 2.1.0
- django-filter 1.0.4
- djangorestframework 3.6.4
- node 6.11.1
- npm 5.3.1
- Angular 4

## SetUp Django

install library
```
$ pip install django
$ pip install djangorestframework
$ pip install django-filter
$ pip install django-cors-headers
```
migration Django
```
$python manage.py makemigrate travelplan
```

migration Django
```
$python manage.py migrate
```

start Django
```
$ cd travel_web_api
$ python manage.py runserver
```

## SetUp Angular4

install npm module
```
$ cd travel_web_app
$ npm install
```

start Angular
```
$ npm start
```
