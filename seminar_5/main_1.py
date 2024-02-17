'''Задание №1
Создать API для управления списком задач. Приложение должно иметь
возможность создавать, обновлять, удалять и получать список задач.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс Task с полями id, title, description и status.
Создайте список tasks для хранения задач.
Создайте маршрут для получения списка задач (метод GET).
Создайте маршрут для создания новой задачи (метод POST).
Создайте маршрут для обновления задачи (метод PUT).
Создайте маршрут для удаления задачи (метод DELETE).
Реализуйте валидацию данных запроса и ответа.''' 
import logging
from fastapi import FastAPI 
from typing import Optional
from pydantic import BaseModel 

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str 
    description: str
    status: str

tasks = [{'id': 1, 'title': 'title1', 'description': 'description1', 'status': 'status1'},
         {'id': 2, 'title': 'title2', 'description': 'description2', 'status': 'status2'},
         {'id': 3, 'title': 'title3', 'description': 'description3', 'status': 'status3'}]



@app.get('/tasks')
async def main_page():
    logger.info('Отработал GET запрос')
    return tasks


@app.post('/task_add/')
async def add_task(task: Task):
    logger.info('Отработал POST запрос')
    tasks.append(task)
    return tasks


@app.put('/task_change/')
async def task_change(task: Task):
    for t in tasks:
        if t["id"] == task.id:
            t["title"] == task.title 
            t["description"] == task.description 
            t["status"] == task.status 
            return tasks 
    return {"response": "This task have not id"}


@app.delete('/delete_task/')
async def delete_task(id: int):
    for i in range(len(tasks)):
        if tasks[i]["id"] == id:
            del tasks[i]
            return tasks 
    return {"response": "This task have not id"}

        
