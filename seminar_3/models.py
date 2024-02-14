from flask_sqlalchemy import SQLAlchemy  

'''Задание №1
Создать базу данных для хранения информации о студентах университета.
База данных должна содержать две таблицы: "Студенты" и "Факультеты".
В таблице "Студенты" должны быть следующие поля: id, имя, фамилия,
возраст, пол, группа и id факультета.
В таблице "Факультеты" должны быть следующие поля: id и название
факультета.
Необходимо создать связь между таблицами "Студенты" и "Факультеты".
Написать функцию-обработчик, которая будет выводить список всех
студентов с указанием их факультета.'''

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), nullable=False)
    second_name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    group = db.Column(db.String(20), nullable=False)
    id_facult = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)

    def __repr__(self):
        return f'Student {self.user_name}, {self.second_name}, {self.age}, {self.gender}' 


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_faculty = db.Column(db.String(20), db.ForeignKey('student.id'), nullable=False) 

    def __repr__(self):
        return f'Faculty{self.name_faculty}' 