'''Задание
Необходимо создать API для управления списком задач. 
Каждая задача должна содержать заголовок и описание. 
Для каждой задачи должна быть возможность указать статус (выполнена/не выполнена).
API должен содержать следующие конечные точки:
— GET /tasks — возвращает список всех задач.
— GET /tasks/{id} — возвращает задачу с указанным идентификатором.
— POST /tasks — добавляет новую задачу.
— PUT /tasks/{id} — обновляет задачу с указанным идентификатором.
— DELETE /tasks/{id} — удаляет задачу с указанным идентификатором.
Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа. 
Для этого использовать библиотеку Pydantic.'''

from fastapi import FastAPI 
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    discription: str
    status: str


tasks = [Task(id=1, title='task_1', discription='buy products in market', status='not done'),
         Task(id=2, title='task_2', discription='make a table in garage', status='not done'),
         Task(id=3, title='task_3', discription='play a football', status='not done')]


@app.get('/tasks')
async def main_page():
    return tasks   


@app.get('/tasks/{id}')
async def main_page(id: int):
    for task in tasks:
        if task.id == id:
            return task 
    return {'response': 'User this id is not defied. Get task impossible'}      


@app.post('/add_task')
async def add_task(task: Task):
    tasks.append(task)
    return tasks


@app.put('/changes_task/{id}')
async def changes_task(id: int):
    for task in tasks:
        if task.id == id:
            task.discription = 'the scheduled task has been completed successfully '
            task.status == 'done'
        return tasks 
    return {'response': 'User this id is not defied. Update task impossible'}    


@app.delete('/delete_task/{id}')
async def delete_task(id: int):
    for task in tasks:
        if task.id == id:
            del task
            return tasks 
    return {'response': 'User this id is not defied. Delete task impossible'}        
