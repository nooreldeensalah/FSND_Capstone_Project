from datetime import datetime

import flask
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from models import setup_db, Movie, Actor
from auth import AuthError, requires_auth


def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    # Request CORS Headers
    @app.after_request
    def after_request(response):
        allowed_headers = "Content-Type,Authorization,true"
        response.headers.add("Access-Control-Allow-Headers", allowed_headers)
        allowed_methods = "GET,PUT,POST,DELETE,OPTIONS"
        response.headers.add("Access-Control-Allow-Methods", allowed_methods)
        return response

    @app.route("/movies")
    def get_movies():
        page = request.args.get("page", 1, type=int)
        movies_per_page = request.args.get("limit", 10, type=int)
        movies = Movie.query.paginate(page, movies_per_page).items
        return jsonify({"movies": [movie.format() for movie in movies]})

    @app.route("/actors")
    def get_actors():
        page = request.args.get("page", 1, type=int)
        actors_per_page = request.args.get("limit", 10, type=int)
        actors = Actor.query.paginate(page, actors_per_page).items
        return jsonify({"actors": [actor.format() for actor in actors]})

    @app.route("/movies", methods=["POST"])
    def insert_movie():
        request_body = request.get_json()
        if any([not request_body[key] for key in request_body]):
            abort(400)
        try:
            title = request_body["title"]
            # Expected datetime format example: "March 11, 1998"
            release_date = datetime.strptime(request_body["release_date"], "%B %d, %Y")
            genre = request_body["genre"]
            movie = Movie(title=title, release_date=release_date, genre=genre)
            movie.insert()
            return flask.Response(status=201)
        except BaseException:
            abort(422)

    @app.route("/actors", methods=["POST"])
    def insert_actor():
        request_body = request.get_json()
        if any([not request_body[key] for key in request_body]):
            abort(400)
        try:
            actor = Actor(**request_body)
            actor.insert()
            return flask.Response(status=201)
        except BaseException:
            abort(422)

    #  DELETE NOTES:
    #  -------------
    #  From this link: https://restfulapi.net/http-methods/#delete
    #  it's stated that DELETE operations with no response should return 204.
    #  I found that the community is divided whether if deleting non-existent resources should return 404, or 204
    #  For the sake of simplicity, I'll use 404.

    @app.route("/movies/<int:movie_id>", methods=["DELETE"])
    def delete_movie(movie_id):
        movie = Movie.query.get(movie_id)
        movie.delete() if movie is not None else abort(404)
        return flask.Response(status=204)

    @app.route("/actors/<int:actor_id>", methods=["DELETE"])
    def delete_actor(actor_id):
        actor = Movie.query.get(actor_id)
        actor.delete() if actor is not None else abort(404)
        return flask.Response(status=204)

    @app.route("/movies/<int:movie_id>", methods=["PUT"])
    def update_movie(movie_id):
        movie = Movie.query.get(movie_id)
        if movie is None:
            abort(404)
        request_body = request.get_json()
        title = request_body.get("title", None)
        genre = request_body.get("genre", None)
        release_date = request_body.get("release_date", None)
        try:
            if title:
                movie.title = title
            if genre:
                movie.genre = genre
            if release_date:
                movie.release_date = datetime.strptime(release_date, "%B %d, %Y")
            movie.update()
        except BaseException:
            abort(422)
        return flask.Response(status=204)

    @app.route("/actors/<int:actor_id>", methods=["PUT"])
    def update_actor(actor_id):
        actor = Actor.query.get(actor_id)
        if actor is None:
            abort(404)
        request_body = request.get_json()
        name = request_body.get("name", None)
        age = request_body.get("age", None)
        gender = request_body.get("gender", None)
        try:
            if name:
                actor.name = name
            if age:
                actor.age = age
            if gender:
                actor.gender = gender
            actor.update()
        except:
            abort(422)
        return flask.Response(status=204)

    # I've designed models to be a many-to-many relationship between actors and movies.
    # For a specific movie, there's a cast of actors.
    # And an actor has a list of movies that he is/was featured in.
    # The first method adds an actor to a movie's cast.
    # The second methods adds a movie to an actor's past/present movies list.
    @app.route("/movies/<int:movie_id>/actors/<int:actor_id>", methods=["POST"])
    def add_actor_to_movie_cast(movie_id, actor_id):
        movie = Movie.query.get(movie_id)
        actor = Actor.query.get(actor_id)
        if actor is None or movie is None:
            abort(404)
        movie.add_actor(actor)
        return flask.Response(status=204)

    @app.route("/actors/<int:actor_id>/movies/<int:movie_id>", methods=["POST"])
    def add_movie_to_actor_movies_list(actor_id, movie_id):
        actor = Actor.query.get(actor_id)
        movie = Movie.query.get(movie_id)
        if actor is None or movie is None:
            abort(404)
        actor.add_movie(movie)
        return flask.Response(status=204)

    return app


APP = create_app()

if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=8080, debug=False)
