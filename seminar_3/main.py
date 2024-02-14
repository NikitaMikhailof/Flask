from flask import Flask, render_template 
 
from models import db, Student, Faculty


app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def main_page():
    return 'Hello'


@app.cli.command("fill-db")
def fill_tables():
    # Добавляем факультеты
    for faculty in range(5):
        new_faculty = Faculty(name_faculty=f'chemistry_{faculty}')
        db.session.add(new_faculty)
    db.session.commit()    

    # Добавляем пользователей
    for student in range(5):
        new_student = Student(user_name=f'user{student}', second_name=f'surname{student}',
                      age=(20 + student), gender='men',
                      group=f'group_{student}', id_facult= student)
        db.session.add(new_student)
    db.session.commit()


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('OK')


@app.route('/information/')
def information():
    students = Student.query.all()
    facultys = Faculty.query.all()
    context = {'students': students, 'facultys': facultys}
    return render_template('information.html', **context)


if __name__ == '__main__':
    app.run()

