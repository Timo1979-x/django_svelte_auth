# Title
[Course](https://www.udemy.com/course/svelte-django-authentication/)

## project setup
### backend
- install python3
- install dependencies:
```
apt install python3-dev default-libmysqlclient-dev build-essential pkg-config mariadb-client python3.12-venv -y
```
- [create project](https://www.django-rest-framework.org/tutorial/quickstart/) :
```bash
mkdir django_svelte_auth && cd django_svelte_auth
python -m venv env
source env/bin/activate
pip install django djangorestframework mysql jwt django-cors-headers
# pip install PyJWT
django-admin startproject app .
django-admin startapp core

```
- run the project:
```
python manage.py runserver
```

### Frontend
```bash
npx degit sveltejs/template svelte-auth
cd svelte-auth
npm i
node scripts/setupTypeScript.js
npm install svelte-spa-router
npm i
```

## Заметки
После каждого изменения модели надо делать миграцию:
```
python manage.py makemigrations
python manage.py migrate
```