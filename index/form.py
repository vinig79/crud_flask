from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired
class Atualizar(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    email = EmailField("email")
    submit = SubmitField("submit")
