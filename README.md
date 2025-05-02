# api_final
Данный api предоставляет возможность пользователям управления такими задачами, как: создание постов, комментариев, их редактирование, удаление и возможность подписываться на пользователей. api имеет простой и интуитивно понятный интерфейс, который вы сможете легко интегрировать в вашу систему. К тому же, данное api обеспечивает безопасность данных с помощью проверки подлинности и авторизации. Можете быть уверены, что ваши данные будут защищены.

## Примеры API-запросов к Django REST Framework (DRF)
GET-запрос (получение списка объектов)

import requests

url = "http://127.0.0.1:8000/api/books/"  # Пример API для книг
response = requests.get(url)

print(response.status_code)  # 200 (OK)
print(response.json())  # Вывод JSON-ответа
С фильтрацией (?author=Толстой):

params = {"author": "Толстой"}
response = requests.get(url, params=params)

POST-запрос (создание объекта)

import requests

url = "http://127.0.0.1:8000/api/books/"
data = {
    "title": "Война и мир",
    "author": "Толстой",
    "year": 1869
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=data, headers=headers)
print(response.status_code)  # 201 (Created)
print(response.json())  # {"id": 1, "title": "Война и мир", ...}
Если API требует токен аутентификации:

headers = {
    "Authorization": "Token ваш_токен",  # Или "Bearer ваш_jwt_токен"
    "Content-Type": "application/json"
}
response = requests.post(url, json=data, headers=headers)
PUT/PATCH-запрос (обновление объекта)

import requests

book_id = 1
url = f"http://127.0.0.1:8000/api/books/{book_id}/"
data = {"year": 1870}  # Изменяем год

PUT (полное обновление) или PATCH (частичное)
response = requests.patch(url, json=data)
print(response.status_code)  # 200 (OK)
DELETE-запрос (удаление объекта)

import requests

book_id = 1
url = f"http://127.0.0.1:8000/api/books/{book_id}/"

response = requests.delete(url)
print(response.status_code)


Раздел "Использованные технологии". В нем можно перечислить
· использованные каркасы (framework) и библиотеки (library)
· с их названиями, ролью в проекте и ссылкой на документацию.
· Это так называемый "стек (технологий)" нашего проекта.
Раздел "Автор". В нем можно указать свои имя, фамилию и ссылку на гитхаб. И даже всю команду в групповом задании.


## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

git clone https://github.com/yandex-praktikum/api_final_yatube.git

Cоздать и активировать виртуальное окружение:

python3 -m venv env
source env/bin/activate
Установить зависимости из файла requirements.txt:

python3 -m pip install --upgrade pip
pip install -r requirements.txt
Выполнить миграции:

python3 manage.py migrate
Запустить проект:

python3 manage.py runserver
