'''Задание №5
Создать страницу, на которой будет форма для ввода двух
чисел и выбор операции (сложение, вычитание, умножение
или деление) и кнопка "Вычислить"
При нажатии на кнопку будет произведено вычисление
результата выбранной операции и переход на страницу с
результатом.'''

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/calculate/', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        num_1 = float(request.form['num_1'])
        num_2 = float(request.form.get('num_2'))
        operation = request.form.get('operation')
        result = 0
        if operation == '+':
            result = num_1 + num_2
        elif operation == '-':
            result = num_1 - num_2
        elif operation == '/':
            result = num_1 / num_2
        else:
            result = num_1 * num_2
        return f'Результат:  {num_1} {operation} {num_2} = {result} '
    return render_template('calculate.html')


if __name__ == '__main__':
    app.run()
    