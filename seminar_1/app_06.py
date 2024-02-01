'''
Задание №6
Написать функцию, которая будет выводить на экран HTML
страницу с таблицей, содержащей информацию о студентах.
Таблица должна содержать следующие поля: "Имя",
"Фамилия", "Возраст", "Средний балл".
Данные о студентах должны быть переданы в шаблон через
контекст.
'''
from flask import render_template
from data_base import students
from app_01 import app 



@app.route('/students/')
def context():
    return render_template('/table.html', students=students)




if __name__ == '__main__':
    app.run()