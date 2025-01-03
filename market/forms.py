from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Length, Email, EqualTo, DataRequired

class RegisterForm(FlaskForm):
    username = StringField(label='Username:', validators=[Length(min=3, max=30), DataRequired()])
    email_address = StringField(label='Email:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[DataRequired(), EqualTo('password1')])
    submit = SubmitField(label='Create Account') 