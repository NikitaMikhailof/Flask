'''Задание №4
Создать API для обновления информации о пользователе в базе данных.
Приложение должно иметь возможность принимать PUT запросы с данными
пользователей и обновлять их в базе данных.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс User с полями id, name, email и password.
Создайте список users для хранения пользователей.
Создайте маршрут для обновления информации о пользователе (метод PUT).
Реализуйте валидацию данных запроса и ответа.'''

from fastapi import FastAPI 
from pydantic import BaseModel 

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str
    password: str 

users = [{'id': 1, 'name': 'Nikita', 'email': 'mikhailofnikita2016@yandex.ru', 'password': '123'},
         {'id': 2, 'name': 'Narta', 'email': 'spaik1989@mail.ru', 'password': '1234'},
         {'id': 3, 'name': 'Mark', 'email': 'mark2021@yandex.ru', 'password': '12345'}] 


@app.get('/')
async def main_page():
    return users 


@app.put('/change_user/')
async def change_user(id: int):
    count = 0
    for user in users:
        if user['id'] == id:
            user['name'] += f' : {count}'
            user['email'] += f' : {count}'
            user['password'] += f' : {count}'
            count += 1 
            return users 
    return {'response': 'User this id is not defied'}
    

@app.delete('/delete_user/')
async def delete_user(id: int):
    for i in range(len(users)):
        if users[i]["id"] == id:
            del users[i]
            return users
    return {"response": "This task have not id"}

        