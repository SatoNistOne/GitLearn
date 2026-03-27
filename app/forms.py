from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, Email, Regexp
from app.models import User

class LoginForm(FlaskForm):
    username_or_email = StringField('Имя пользователя или Email', 
        validators=[
            DataRequired(), 
            Length(min=3, max=128, message='Длина от 3 до 128 символов')
        ])
    password = PasswordField('Пароль', 
        validators=[
            DataRequired(),
            Length(min=6, max=128, message='Пароль должен быть от 6 до 128 символов')
        ])
    submit = SubmitField('Войти')

class RegisterForm(FlaskForm):
    username = StringField('Имя пользователя', 
        validators=[
            DataRequired(), 
            Length(min=3, max=64, message='Имя должно быть от 3 до 64 символов'),
            Regexp('^[a-zA-Zа-яА-Я0-9_]+$', message='Только буквы, цифры и подчёркивание')
        ])
    email = EmailField('Email', 
        validators=[
            DataRequired(), 
            Email(message='Введите корректный email'),
            Length(max=128, message='Email не должен превышать 128 символов')
        ])
    password = PasswordField('Пароль', 
        validators=[
            DataRequired(),
            Length(min=6, max=128, message='Пароль должен быть от 6 до 128 символов')
        ])
    confirm_password = PasswordField('Подтвердите пароль', 
        validators=[
            DataRequired(), 
            EqualTo('password', message='Пароли должны совпадать')
        ])
    submit = SubmitField('Зарегистрироваться')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Это имя пользователя уже занято')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Этот email уже зарегистрирован')
