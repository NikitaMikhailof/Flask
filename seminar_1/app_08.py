'''
Задание №8
Создать базовый шаблон для всего сайта, содержащий
общие элементы дизайна (шапка, меню, подвал), и
дочерние шаблоны для каждой отдельной страницы.
Например, создать страницу "О нас" и "Контакты",
используя базовый шаблон.
'''

from app_01 import app 
from flask import render_template


@app.route('/')
def page():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/contact/')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()