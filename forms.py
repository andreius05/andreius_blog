from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from flaskblog.models import User
from flask_login import current_user




class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self,username):
        user = User.query.filter_by(username =username.data).first()
        if user:
            raise ValidationError('That username is taken')

    def validate_email(self,email):
        user = User.query.filter_by(email =email.data).first()
        if user:
            raise ValidationError('That email is taken')




class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')



class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update account image',validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    def validate_username(self,username):
        if username.data != current_user.username:
            user = User.query.filter_by(username =username.data).first()
            if user:
                raise ValidationError('That username is taken')

    def validate_email(self,email):
        if email.data!=current_user.email:
            user = User.query.filter_by(email =email.data).first()
            if user:
                raise ValidationError('That email is taken')


class PostForm(FlaskForm):
    title = StringField('TItle',validators=[DataRequired()])
    content = TextAreaField('Content',validators = [DataRequired()])
    submit = SubmitField('Post')



class RequestResetForm(FlaskForm):
     email = StringField('Email', validators=[DataRequired(), Email()])
     submit = SubmitField('Request to reset password(')
     def validate_email(self,email):

        user = User.query.filter_by(email =email.data).first()
        if user is None:
            raise ValidationError('There is no account with this email')


class ResetPassword(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset password')