'''
Задание №4
Написать функцию, которая будет принимать на вход строку и
выводить на экран ее длину.
'''

from app_01 import app


@app.route('/string/<text>/')
def lenght_string(text: str):
    return str(len(text))


if __name__ == '__main__':
    app.run()