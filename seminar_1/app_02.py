'''
Задание №2
Дорабатываем задачу 1.
Добавьте две дополнительные страницы в ваше веб-приложение:
страницу "about"
страницу "contact".
'''
from app_01 import app


@app.route('/about/')
def about():
    return 'about'



@app.route('/contact/')
def contact():
    return 'contact'



if __name__ == '__main__':
    app.run()
