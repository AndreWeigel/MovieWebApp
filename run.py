from flask import Flask
from flask import request, redirect, url_for, render_template

from app.models import db


# ⚠️ IMPORT models before calling db.create_all()
from app.models.user import User
from app.models.movie import Movie

from app.services.user import UserService
from app.services.movie import MovieService
from app.routes.user import user_routes
from app.routes.movie import movie_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

user_service = UserService()
movie_serv = MovieService()

@app.route('/')
def home():
    return redirect(url_for('user_routes.index'))

app.register_blueprint(user_routes)
app.register_blueprint(movie_routes)


with app.app_context():
    db.create_all()

if __name__ == '__main__':

    app.run()
