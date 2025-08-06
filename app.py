from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms.fields.numeric import DecimalField
from wtforms.fields.simple import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email, NumberRange

app = Flask(__name__)

# Configure SQLite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = 'my-fixed-secret-key-for-development'

# Initialize SQLAlchemy
db = SQLAlchemy(app)


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


@app.route("/register", methods=["POST","GET"])
def register_page():
    form = UserForm()
    return render_template("register.html", form= form)

@app.route("/login", methods=["POST","GET"])
def login_page():
    form = UserForm()
    return render_template("login.html", form= form)


@app.route("/dashboard", methods=["POST","GET"])
def dashboard_page():
    form = ParcelForm()
    return render_template("dashboard.html", form= form)

@app.route("/profile")
def profile_page():
    return render_template("profile.html")


@app.route("/admin")
def admin_page():
    return render_template("admin.html")

# Start the app
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
