from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import TextAreaField
from wtforms.validators import DataRequired

# Add any form classes for Flask-WTF here

class UploadForm(FlaskForm):

    description = TextAreaField('Description', validators=[DataRequired('Description of picture is required')])
    photo = FileField('Photo', validators= [FileRequired(message="An image file is required."),
            FileAllowed(['jpg','jpeg', 'png'], 'Images only!')

    ])

    

