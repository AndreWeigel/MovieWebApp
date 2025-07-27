from app.models import db
from app.models.movie import Movie
from sqlalchemy.exc import SQLAlchemyError
import os
import requests
from dotenv import load_dotenv
load_dotenv()


class MovieService:
    OMDB_API_KEY = os.getenv("OMDB_API_KEY")
    @staticmethod
    def create_movie(title, director, year=None, poster_url=None, user_id=None):
        try:
            movie = Movie(
                title=title,
                director=director,
                year=year,
                poster_url=poster_url,
                user_id=user_id
            )
            db.session.add(movie)
            db.session.commit()
            return movie
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Error creating movie: {e}")

    @staticmethod
    def get_movie_by_id(movie_id):
        return Movie.query.get(movie_id)

    @staticmethod
    def get_all_movies():
        return Movie.query.all()

    @staticmethod
    def get_movies_by_user(user_id):
        return Movie.query.filter_by(user_id=user_id).all()

    @staticmethod
    def update_movie(movie_id, title=None, director=None, year=None, poster_url=None):
        movie = Movie.query.get(movie_id)
        if not movie:
            return None

        if title is not None:
            movie.title = title
        if director is not None:
            movie.director = director
        if year is not None:
            movie.year = year
        if poster_url is not None:
            movie.poster_url = poster_url

        try:
            db.session.commit()
            return movie
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Error updating movie: {e}")

    @staticmethod
    def delete_movie( user_id, movie_id):
        movie = Movie.query.get(movie_id)
        if not movie:
            return False  # Movie doesn't exist
        if movie.user_id != user_id:
            return False  # Unauthorized deletion attempt

        try:
            db.session.delete(movie)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Error deleting movie: {e}")

    @staticmethod
    def search_omdb_movies(title, year=None):
        params = {
            "apikey": MovieService.OMDB_API_KEY,
            "s": title,
            "type": "movie"
        }
        if year:
            params["y"] = year

        try:
            response = requests.get("http://www.omdbapi.com/", params=params)
            response.raise_for_status()
            data = response.json()
            if data.get("Response") == "True":
                return data["Search"]  # List of movies
            else:
                return []
        except requests.RequestException as e:
            raise Exception(f"Error fetching data from OMDB: {e}")

    @staticmethod
    def add_omdb_movie_to_db(imdb_id, user_id=None):
        params = {
            "apikey": MovieService.OMDB_API_KEY,
            "i": imdb_id,
            "plot": "short"
        }

        try:
            response = requests.get("http://www.omdbapi.com/", params=params)
            response.raise_for_status()
            data = response.json()

            if data.get("Response") != "True":
                raise Exception("Movie not found in OMDB")

            title = data.get("Title")
            director = data.get("Director", "Unknown")
            year = int(data["Year"].split("–")[0]) if data.get("Year") else None
            poster_url = data.get("Poster") if data.get("Poster") != "N/A" else None

            return MovieService.create_movie(
                title=title,
                director=director,
                year=year,
                poster_url=poster_url,
                user_id=user_id
            )
        except requests.RequestException as e:
            raise Exception(f"Error fetching movie details from OMDB: {e}")


if __name__ == '__main__':
    movie_service = MovieService()

    res = movie_service.search_omdb_movies('Matrix')
    for i in res:
        print(i)

