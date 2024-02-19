'''Необходимо создать базу данных для интернет-магазина. 
База данных должна состоять из трёх таблиц: товары, заказы и пользователи.
— Таблица «Товары» должна содержать информацию о доступных товарах, их описаниях и ценах.
— Таблица «Заказы» должна содержать информацию о заказах, сделанных пользователями.
— Таблица «Пользователи» должна содержать информацию о зарегистрированных пользователях магазина.
• Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.
• Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус заказа.
• Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.
Создайте модели pydantic для получения новых данных и возврата существующих в БД для каждой из трёх таблиц.
Реализуйте CRUD операции для каждой из таблиц через создание маршрутов, REST API.'''

import databases
from sqlalchemy import Table, Column, Integer, String, Float, DateTime, MetaData, ForeignKey, create_engine
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr
from typing import Literal
from datetime import datetime

DATABASE_URL = "sqlite:///my_database.db"
database = databases.Database(DATABASE_URL)
metadata = MetaData()

users = Table("users", metadata, Column("id", Integer,
                        primary_key=True),
                        Column("name", String(30)),
                        Column("second_name", String(30)),
                        Column("email", String(30)),
                        Column("password", String(30)),
)

orders = Table("orders", metadata, Column("id", Integer,
                        primary_key=True),
                        Column("user_id", Integer, ForeignKey("users.id")),
                        Column("product_id", Integer, ForeignKey("products.id")),
                        Column("data", DateTime),
                        Column("status", String(10)),
)

products = Table("products", metadata, Column("id", Integer,
                        primary_key=True),
                        Column("name", String(30)),
                        Column("discription", String(30)),
                        Column("price", Float),
)

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)
app = FastAPI()

class User(BaseModel):
    id:int
    name:str = Field(title='name', max_length=30)
    second_name:str = Field(title='second_name', max_length=30)
    email:EmailStr = Field(title='Email', max_length=30)
    password:str = Field(title='Password', min_length=6, max_length=30)



class Order(BaseModel):
    id:int
    user_id:int
    products_id:int
    data:str = Field(title='data')
    status:Literal['done', 'not done']

class Product(BaseModel):
    id:int
    name:str = Field(title='name', max_length=30)
    discription:str = Field(title='discription', max_length=30)
    price:float = Field(title='price')


@app.get("/users/", response_model=list[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


@app.get('/users/{user_id}', response_model=User)
async def read_all_users(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@app.post('/users/', response_model=User)
async def create_user(user: User):
    query = users.insert().values(name=user.name, second_name=user.second_name, email=user.email, password=user.password)
    last_record_id = await database.execute(query)
    return{**user.dict(), 'id':last_record_id}


@app.put('/users/{user_id}', response_model=User)
async def update_user(user_id: int, new_user: User):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    await database.execute(query)
    return{**new_user.dict(), 'id': user_id}


@app.delete('/users/{user_id}/')
async def delete_user(user_id : int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return{'message': 'User deleted'}
   

@app.post('/users_buy/{user_id}/{products_name}') 
async def users_buy(user_id: int, products_name: str):
    query_users = users.select().where(users.c.id == user_id)
    query_products = products.select().where(products.c.name == products_name)
    res1 = await database.fetch_one(query_users)
    res2 = await database.fetch_one(query_products)
    if res1 and res2:
        query = orders.insert().values(user_id = res1['id'], product_id = res2['id'], data = datetime.utcnow(), status='done') 
        await database.execute(query)
        return{'message': f'User:  {res1['name']} made purchases'} 
    return{'message': 'User with {id_user} or {id_products} not defined'}
    

@app.delete('/users_buy/{order_id}')
async def users_buy_delete(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return{'message': 'Order deleted'}
