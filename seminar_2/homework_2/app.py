'''Задание №6
Создать страницу, на которой будет форма для ввода имени
и возраста пользователя и кнопка "Отправить"
При нажатии на кнопку будет произведена проверка
возраста и переход на страницу с результатом или на
страницу с ошибкой в случае некорректного возраста.'''


from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        age = int(request.form.get('age'))
        if age > 0 and age < 100:
            return render_template('age_result.html', age=age, name=name.capitalize())
        else:
            return render_template('age_error.html', age=age)
    return render_template('form.html')



@app.route('/age_error/')
def age_error():
    return render_template('age_error.html')


@app.route('/age_result/')
def age_result():
    return render_template('age_result.html')


if __name__ == '__main__':
    app.run(debug=True)
