'''Задание №2
Создать API для получения списка фильмов по жанру. Приложение должно
иметь возможность получать список фильмов по заданному жанру.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс Movie с полями id, title, description и genre.
Создайте список movies для хранения фильмов.
Создайте маршрут для получения списка фильмов по жанру (метод GET).
Реализуйте валидацию данных запроса и ответа.'''

from fastapi import FastAPI 
from pydantic import BaseModel

app = FastAPI()

class Movie(BaseModel):
    id : int
    title: str
    description: str
    genre: str 

movies = [{'id': 1, 'title': 'Rocky', 'description': 'Film about boxer', 'genre': 'drama'},
          {'id': 2, 'title': 'Scala', 'description': 'Film about spy agent', 'genre': 'blokbaster'},
          {'id': 3, 'title': 'Operation iu', 'description': 'Film about three crook', 'genre': 'comedy'}]


@app.get('/')
async def main_page():
    return {'это': 'сайт с фильмами'}


@app.get('/films/')
async def films():
    return movies 


@app.post('/film_add/')
async def film_add(movie: Movie):
    movies.append(movie)
    return  movies 


@app.put('/change_films/')
async def change_films():
    for movie in movies:
        if movie['genre'] == 'drama':
            movie['title'] = 'Pirates caribian sea'
            movie['description'] = 'Film about pirates'
            movie['genre'] = 'adventures'
            return movies 
    return {'response': 'This is genre is not defined'}


@app.delete('/delete_film/')
async def delete_movie():
    for i in range(len(movies)):
        if movies[i]['title'] == 'Pirates caribian sea':
            del movie 
            return movies 
    return {'response': 'This id is not defined'}    


