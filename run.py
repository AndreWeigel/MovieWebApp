from flask import Flask
from app.models import db

# ⚠️ IMPORT models before calling db.create_all()
from app.models.user import User
from app.models.movie import Movie

from app.services.user import UserService
from app.services.movie import MovieService

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

user_service = UserService()
movie_serv = MovieService()

@app.route('/')
def home():
    return "Welcome to MovieWeb App!"

@app.route('/users')
def list_users():
    users = user_service.get_users()
    return str(users)

with app.app_context():
    db.create_all()

if __name__ == '__main__':

    app.run()
