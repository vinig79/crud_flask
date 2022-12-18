from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class Register(FlaskForm):
    nome = StringField("name", validators=[DataRequired()])
    email = EmailField("email")
    password = PasswordField("password")
    submit = SubmitField("submit")
