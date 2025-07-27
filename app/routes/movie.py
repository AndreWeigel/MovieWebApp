from flask import Blueprint, render_template, request, redirect, url_for
from app.services.movie import MovieService
from app.services.user import UserService

movie_routes = Blueprint('movie_routes', __name__)

# View all movies for a user
@movie_routes.route('/users/<int:user_id>/movies', methods=['GET'])
def get_movies(user_id):
    user = UserService.get_user_by_id(user_id)
    movies = MovieService.get_movies_by_user(user_id)
    return render_template('movies.html', user=user, movies=movies)

@movie_routes.route('/users/<int:user_id>/search-movie', methods=['GET', 'POST'])
def search_movie(user_id):
    suggestions = []
    query = ""

    if request.method == 'POST':
        query = request.form.get('query')
        if query:
            suggestions = MovieService.search_omdb_movies(query)

    user = UserService.get_user_by_id(user_id)
    return render_template('search_movie.html', user=user, query=query, suggestions=suggestions)

# Add a new movie for a user
@movie_routes.route('/users/<int:user_id>/add-movie', methods=['POST'])
def add_movie(user_id):
    imdb_id = request.form.get('imdb_id')
    if imdb_id:
        print(imdb_id)
        MovieService.add_omdb_movie_to_db(imdb_id,user_id)
    return redirect(url_for('movie_routes.get_movies', user_id=user_id))

# Delete a movie for a user
@movie_routes.route('/users/<int:user_id>/delete-movie/<int:movie_id>', methods=['POST'])
def delete_movie(user_id, movie_id):
    MovieService.delete_movie(user_id, movie_id)
    return redirect(url_for('movie_routes.get_movies', user_id=user_id))
