'''Задание №1
Создать страницу, на которой будет кнопка "Нажми меня", при
нажатии на которую будет переход на другую страницу с
приветствием пользователя по имени.'''

from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)


@app.route('/button/')
def button_page():
    return render_template('button.html')


@app.route('/')
def main_page():
    name = 'Nikita'
    return f'Hello {name}'  



if __name__ == '__main__':
    app.run()