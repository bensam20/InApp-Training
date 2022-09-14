
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Declaring the database uri as the key into flask config object
#mssql+pyodbc://server/dbname?driver=driver
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://DESKTOP-CSCIVVL\SQLEXPRESS/empdb?driver=SQL+Server+Native+Client+11.0'
#track modification key to false to optimise memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#set the secret key for the forms
app.config['SECRET_KEY'] = 'my secret key'

#instatiate the db object
db = SQLAlchemy(app)

#create a class for the model. Class name will be table name and attributes will be the columns
class Employees(db.Model):
    id = db.Column('employee_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    salary = db.Column(db.Float(50))
    age = db.Column(db.String(50))

    #define constructor
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age

#route to list all employees
@app.route('/')
def list_employees():
    return render_template('list.html',Employees=Employees.query.all())

#route to add new employee
@app.route('/add', methods=['GET','POST'])
def addEmployee():
    #checking if the form was submitted by post method / by clicking the button
    if request.method == 'POST':
        if not request.form['name'] or not request.form['salary'] or not request.form['age']:
            flash('Please enter all the fields','error')
            return redirect(url_for('addEmployee'))
        else:
            #if all the variables are set, we will proceed with data adding
            #create an instance of Employees
            employee = Employees(request.form['name'], request.form['salary'], request.form['age'])
            #add and commit the row of data to the Employees table 
            db.session.add(employee)
            db.session.commit()
            return redirect(url_for('list_employees'))
    #if the user is accessing the page directly, give the template add.html
    return render_template('add.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)