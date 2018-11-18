from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField  , SubmitField , BooleanField , TextAreaField
from wtforms.validators import DataRequired , Length , Email , EqualTo ,ValidationError
from flaskblog.models import User
from flask_login import current_user
from flask_wtf.file import FileField , FileAllowed

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired() ,Length(min=2 , max=20)] )
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Passowrd', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                      validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username is taken . Pls choose different one.')
    
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email is taken . Pls choose different one.')
    

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Passowrd', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired() ,Length(min=2 , max=20)] )
    email = StringField('Email', validators=[DataRequired(),Email()])
    picture = FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    def validate_username(self,username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('This username is taken . Pls choose different one.')
    
    def validate_email(self,email):
        if email.data != current_user.email:    
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('This email is taken . Pls choose different one.')

class PostForm(FlaskForm):
    title = StringField('Title' , validators=[DataRequired()])
    content = TextAreaField('Content',validators=[DataRequired()])
    submit = SubmitField('Post')
