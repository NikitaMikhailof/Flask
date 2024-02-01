'''
Задание №3
Написать функцию, которая будет принимать на вход два
числа и выводить на экран их сумму.
'''

from app_01 import app



@app.route('/summ/<int:a>/<int:b>/')
def summ(a, b):
    return str(a + b)


if __name__ == '__main__':
    app.run()