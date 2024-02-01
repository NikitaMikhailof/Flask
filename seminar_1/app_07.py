'''
Задание №7
Написать функцию, которая будет выводить на экран HTML
страницу с блоками новостей.
Каждый блок должен содержать заголовок новости,
краткое описание и дату публикации.
Данные о новостях должны быть переданы в шаблон через
контекст.
'''
from data_base import news
from flask import render_template
from app_01 import app 

@app.route('/news/')
def get_news():
    return render_template('news.html', news=news)


if __name__ == '__main__':
    app.run()

