from flask_wtf import FlaskForm
from model import User
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError


class Register(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    email = EmailField("email", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    password_r = PasswordField("Repeat Password", validators=[EqualTo('password'), DataRequired()])
    submit = SubmitField("submit")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("use other email")