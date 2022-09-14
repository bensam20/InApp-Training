from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField

#creating the form class inheriting from FlaskForm
class NameForm(FlaskForm):
    #StringField class represents the text field of html
    #creating the object for the class StringField and have validators attatched
    name = StringField('Enter your name', validators=[DataRequired()])
    filename =  FileField('Upload file')
    #SubmitField class represents the input type submit of html
    submit = SubmitField('submit')
