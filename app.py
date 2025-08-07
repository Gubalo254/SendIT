from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import init_routes
app = Flask(__name__)

# Configure SQLite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sendIT.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = 'f5dcc83eea0f0d80b6a9217929b465432c780d071852c83d'

# Initialize SQLAlchemy
db = SQLAlchemy(app)

init_routes(app)


# Start the app
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
