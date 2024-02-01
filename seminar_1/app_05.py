'''
Задание №5
Написать функцию, которая будет выводить на экран HTML
страницу с заголовком "Моя первая HTML страница" и
абзацем "Привет, мир!".
'''

from app_01 import app


@app.route('/first HTML/')
def first_html():
    text = ['Моя первая HTML страница', 'Привет, мир!']
    return f'<h1>{text[0]}<h1>\n<h2>{text[1]}</h2>'



if __name__ == '__main__':
    app.run()