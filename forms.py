from flask_wtf import FlaskForm
from wtforms.fields.numeric import DecimalField
from wtforms.fields.simple import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email, NumberRange

class MapsForm(FlaskForm):
    pickup = StringField('Pickup Location', validators=[DataRequired()])
    destination = StringField('Destination', validators=[DataRequired()])
    submit = SubmitField('Show Route')

class UserForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired(message='User name is required'), Length(max=40)])
    email = StringField('Email', validators=[DataRequired(message='User email is required'), Email(), Length(max=80)])
    password = PasswordField('Password', validators=[DataRequired(message='User password is required'), Length(min=6)])
    confirm_password = PasswordField('Verify Password', validators=[DataRequired(message='Password confirmation is required'), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message='User email is required'), Email(), Length(max=80)])
    password = PasswordField('Password', validators=[DataRequired(message='User password is required')])
    submit = SubmitField('Login')

class ParcelForm(FlaskForm):
    pickup_location = StringField('Pickup Location', validators=[DataRequired(message="Pickup location is required."),Length(max=100)  ])
    destination = StringField('Destination',validators=[DataRequired(message="Destination is required."),  Length(max=100) ])
    weight = DecimalField( 'Weight (kg)', validators=[     DataRequired(message="Weight is required."), NumberRange(min=0.1, message="Weight must be greater than 0.")],places=2 ) # to allow decimal input like 1.25 kg
    submit = SubmitField('Send Parcel')