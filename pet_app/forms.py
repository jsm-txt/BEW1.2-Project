from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField, PasswordField, SubmitField, ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL

from pet_app.models import User


class NewPetForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired(), Length(min=3, max=50)])
    photo_url = StringField('Photo_url',validators=[URL()])
    submit = SubmitField('SuBmIt')

class ImagesForm(FlaskForm):
    caption = StringField('Caption',validators=[DataRequired(), Length(min=3, max=50)])
    photo_url = StringField('Images_of',validators=[URL()])
    submit = SubmitField('SuBmIt')


class SignUpForm(FlaskForm):
    username = StringField('User Name',
        validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    username = StringField('User Name',
        validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')
