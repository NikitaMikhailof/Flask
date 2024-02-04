'''Задание №2
Создать страницу, на которой будет изображение и ссылка
на другую страницу, на которой будет отображаться форма
для загрузки изображений.'''

from flask import Flask, render_template, request 



app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/img_post/', methods=['GET', 'POST'])
def post_img():
    if request.method == 'POST':
        result = request.files['file']
        print(result)
        return 'Файл загружен'
    return render_template('form.html')        
  

if __name__ == '__main__':
    app.run()