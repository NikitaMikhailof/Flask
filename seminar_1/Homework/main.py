'''Задание №9
Создать базовый шаблон для интернет-магазина,
содержащий общие элементы дизайна (шапка, меню,
подвал), и дочерние шаблоны для страниц категорий
товаров и отдельных товаров.
Например, создать страницы "Одежда", "Обувь" и "Куртка",
используя базовый шаблон.'''


from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def base_page():
    return render_template('index.html')


@app.route('/foot/')
def foot():
    return render_template('foot.html')


@app.route('/jacket/')
def jacket():
    return render_template('jacket.html')


@app.route('/wear/')
def wear():
    return render_template('wear.html')



if __name__ == '__main__':
    app.run()

