'''Разработать API для управления списком пользователей с
использованием базы данных SQLite. Для этого создайте
модель User со следующими полями:
○ id: int (идентификатор пользователя, генерируется
автоматически)
○ username: str (имя пользователя)
○ email: str (электронная почта пользователя)
○ password: str (пароль пользователя)
API должно поддерживать следующие операции:
○ Получение списка всех пользователей: GET /users/
○ Получение информации о конкретном пользователе: GET /users/{user_id}/
○ Создание нового пользователя: POST /users/
○ Обновление информации о пользователе: PUT /users/{user_id}/
○ Удаление пользователя: DELETE /users/{user_id}/
Для валидации данных используйте параметры Field модели User.
Для работы с базой данных используйте SQLAlchemy и модуль databases.
'''
import databases
import sqlalchemy
from fastapi import FastAPI 
from pydantic import BaseModel, Field 

DATABASE_URL = "sqlite:///database.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

users = sqlalchemy.Table("users", metadata, sqlalchemy.Column("id", sqlalchemy.Integer,
                        primary_key=True),
                        sqlalchemy.Column("username", sqlalchemy.String(30)),
                        sqlalchemy.Column("email", sqlalchemy.String(30)),
                        sqlalchemy.Column("password", sqlalchemy.String(30)),
)

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)

app = FastAPI()

class User(BaseModel):
    username:str = Field(title='Username', max_length=30)
    email: str = Field(title='Email', max_length=30)
    password: str = Field(title='Password', min_length=6, max_length=30)

class UserID(User):
    id: int
   

@app.get('/users/', response_model=list[User])
async def read_all_users():
    query = users.select()
    return await database.fetch_all(query)


@app.get('/users/{user_id}', response_model=User)
async def read_all_users(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@app.post('/users/', response_model=User)
async def create_user(user: UserID):
    query = users.insert().values(username=user.username, email=user.email, password=user.password)
    last_record_id = await database.execute(query)
    return{**user.dict(), 'id':last_record_id}
    

@app.put('/users/{user_id}', response_model=UserID)
async def update_user(user_id: int, new_user: UserID):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    await database.execute(query)
    return{**new_user.dict(), 'id': user_id}


@app.delete('/users/{user_id}/')
async def delete_user(user_id : int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return{'message': 'User deleted'}

