from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField

class RegisterForm(FlaskForm):
    username = StringField(label='Username:')
    email_address = StringField(label='Email:')
    password1 = PasswordField(label='Password:')
    password2 = PasswordField(label='Confirm Password:')
    submit = SubmitField(label='Submit') 