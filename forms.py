from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, Text 
from wtforms.validators import DataRequired, Length



class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Length(min=6, max=120)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(min=6, max=120)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ExerciseForm(FlaskForm):
    description = TextAreaField('Exercise Description', validators=[DataRequired()])
    submit = SubmitField('Log Exercise')
