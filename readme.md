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
pip install django djangorestframework mysql jwt django-cors-headers pyotp google-auth
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
npm install svelte-spa-router axios qrcode
npm i
```

## Заметки
После каждого изменения модели надо делать миграцию:
```
python manage.py makemigrations
python manage.py migrate
```

Для настройки учетных данных для аутентификации google нужно:
  - зайти на https://console.cloud.google.com/cloud-resource-manager и создать новый проект My App
  - зайти на https://console.cloud.google.com/apis/credentials/consent. Там настроить Consent screen:
    - User type: External
    - App name: My App
    - user support email: выбрать из списка один из адресов
    - developer contact email:
  - зайти на страницу https://console.cloud.google.com/apis/credentials ("Credentials for APIs and services").
  - Выбрать проект
  - Нажать Create Credentials -> OAuth client ID:
    - Application type: web
    - name: My App
    - Authorized JavaScript origins: http://127.0.0.1:8080, http://localhost:8080
    - нажать Create
    - записать client_id, client_secret
