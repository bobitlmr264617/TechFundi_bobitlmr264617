from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'traceit/postgres@jesse'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class contacts(db.Model):
   number = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   location = db.Column(db.String(200)) 

def __init__(self, number, name, location):
   self.number = number
   self.name = name
   self.location = location
   self.pin = pin

@app.route('/')
def show_all():
   return render_template('success.html', contacts = contacts.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['location'] or not request.form['number']:
         flash('Please enter all the fields', 'error')
      else:
         student = students(request.form['name'], request.form['location'],
            request.form['number'], request.form[])
         


if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)