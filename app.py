from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from models import setup_db


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
        pass

    @app.route("/actors")
    def get_actors():
        pass

    @app.route("/movies", methods=["POST"])
    def insert_movie():
        pass

    @app.route("/actors", methods=["POST"])
    def insert_actor():
        pass

    @app.route("/movies/<int:movie_id>", methods=["DELETE"])
    def delete_movie(movie_id):
        pass

    @app.route("/actors/<int:actor_id>", methods=["DELETE"])
    def delete_actor(actor_id):
        pass

    @app.route("/movies/<int:movie_id>", methods=["PUT"])
    def update_movie(movie_id):
        pass

    @app.route("/actors/<int:actor_id>", methods=["PUT"])
    def update_actor(actor_id):
        pass

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
