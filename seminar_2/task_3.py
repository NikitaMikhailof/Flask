'''Задание №3
Создать страницу, на которой будет форма для ввода логина
и пароля
При нажатии на кнопку "Отправить" будет произведена
проверка соответствия логина и пароля и переход на
страницу приветствия пользователя или страницу с
ошибкой.'''

from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)


@app.route('/')
def start_page():
    return render_template('index.html')


@app.route('/form/', methods={'GET', 'POST'})
def form():
    if request.method == 'POST':
        login, password = 'login', 'password'
        log = request.form.get('login')
        pas = request.form.get('password')
        if log == login and pas == password:
            return redirect(url_for('hi_user'))
        return render_template('error.html')
    return render_template('form_page.html')


@app.route('/hi_user/')
def hi_user():
    return render_template('hi_user.html')


if __name__ == '__main__':
    app.run(debug=True)
