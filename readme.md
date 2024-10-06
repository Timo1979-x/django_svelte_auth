# Title
[Course](https://www.udemy.com/course/svelte-django-authentication/)

## project setup
- install python3
- install dependencies:
```
apt install python3-dev default-libmysqlclient-dev build-essential pkg-config mariadb-client -y
```
- [create project](https://www.django-rest-framework.org/tutorial/quickstart/) :
```bash
mkdir django_vue && cd django_vue
python -m venv env
source env/bin/activate
pip install django djangorestframework mysql
django-admin startproject app .
django-admin startapp core

```
- run the project:
```
python manage.py runserver
```

## Заметки
После каждого изменения модели надо делать миграцию:
```
python manage.py makemigrations
python manage.py migrate
```