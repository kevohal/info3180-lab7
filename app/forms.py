from tkinter import PhotoImage
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import TextAreaField
from wtforms.validators import InputRequired

# Add any form classes for Flask-WTF here

class UploadForm(FlaskForm):

    photo = FileField('Photo', validators= [FileRequired(),
            FileAllowed(['jpg','jpeg', 'png'], 'Images only!')

    ])

    description = TextAreaField('Description', validators=[InputRequired()])

