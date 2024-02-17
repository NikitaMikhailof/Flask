'''Задание №6
Создать веб-страницу для отображения списка пользователей. Приложение
должно использовать шаблонизатор Jinja для динамического формирования HTML
страницы.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс User с полями id, name, email и password.
Создайте список users для хранения пользователей.
Создайте HTML шаблон для отображения списка пользователей. Шаблон должен
содержать заголовок страницы, таблицу со списком пользователей и кнопку для
добавления нового пользователя.
Создайте маршрут для отображения списка пользователей (метод GET).
Реализуйте вывод списка пользователей через шаблонизатор Jinja''' 

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import BaseModel, EmailStr 
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='Flask/seminar_5/templates')

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    password: str 

users = [{'id': 1, 'name': 'Nikita', 'email': 'mikhailoffnikita2016@yandex.ru', 'password': '123' },
         {'id': 2, 'name': 'Marta', 'email': 'marta1991@yandex.ru', 'password': '1234'},
         {'id': 3, 'name': 'Nikita', 'email': 'mark2021@yandex.ru', 'password': '12345'}]


@app.get('/', response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("item.html", {"request": request, "users": users})


@app.put('/add_user/')
async def add_user(user: User):
    users.append(user) 
    return templates.TemplateResponse('Создан новый пользователь')


@app.get('/get_users/', response_class=HTMLResponse)
async def get_users(request: Request):
    return templates.TemplateResponse('item.html', {"request": request, 'users': users})