from flask import render_template, request
from forms import MapsForm,UserForm,ParcelForm

def init_routes(app):
    @app.route('/', methods=['GET', 'POST'])
    def index():
        form = MapsForm()
        pickup = ''
        destination = ''
        if form.validate_on_submit():
            pickup = form.pickup.data
            destination = form.destination.data
        return render_template("maps.html", form=form, pickup=pickup, destination=destination)

    @app.route("/register", methods=["POST", "GET"])
    def register_page():
        form = UserForm()
        return render_template("register.html", form=form)

    @app.route("/login", methods=["POST", "GET"])
    def login_page():
        form = UserForm()
        return render_template("login.html", form=form)

    @app.route("/dashboard", methods=["POST", "GET"])
    def dashboard_page():
        form = ParcelForm()
        return render_template("dashboard.html", form=form)

    @app.route("/profile")
    def profile_page():
        return render_template("profile.html")

    @app.route("/admin")
    def admin_page():
        return render_template("admin.html")