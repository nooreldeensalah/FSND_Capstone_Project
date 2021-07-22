import os
import unittest
from datetime import datetime
from app import create_app
from models import Movie, Actor, setup_db
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
TEST_DB_CONNECTION_STRING = os.getenv("TEST_DB_CONNECTION_STRING")

CASTING_ASSISTANT_TOKEN = os.getenv("CASTING_ASSISTANT_TOKEN")
CASTING_DIRECTOR_TOKEN = os.getenv("CASTING_DIRECTOR_TOKEN")
EXECUTIVE_PRODUCER_TOKEN = os.getenv("EXECUTIVE_PRODUCER_TOKEN")


def create_headers(token):
    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }


class CastingAgencyTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        setup_db(self.app, TEST_DB_CONNECTION_STRING)

    def test_get_movies(self):
        response = self.client.get(
            "/movies",
            headers=create_headers(EXECUTIVE_PRODUCER_TOKEN))
        data = response.get_json()
        movies = data.get("movies", None)

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(movies)

    def test_get_movies_invalid_page(self):
        response = self.client.get(
            "/movies?page=99999",
            headers=create_headers(EXECUTIVE_PRODUCER_TOKEN)
        )
        data = response.get_json()
        movies = data.get("movies", None)

        self.assertEqual(response.status_code, 404)
        self.assertIsNone(movies)

    def test_get_actors(self):
        response = self.client.get(
            "/actors",
            headers=create_headers(EXECUTIVE_PRODUCER_TOKEN))
        data = response.get_json()
        actors = data.get("actors", None)

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(actors)

    def test_get_actors_invalid_page(self):
        response = self.client.get(
            "/actors?page=99999",
            headers=create_headers(EXECUTIVE_PRODUCER_TOKEN)
        )
        data = response.get_json()
        actors = data.get("actors", None)

        self.assertEqual(response.status_code, 404)
        self.assertIsNone(actors)

    def test_add_new_movie(self):
        response = self.client.post(
            "/movies",
            headers=create_headers(EXECUTIVE_PRODUCER_TOKEN),
            json={
                "title": "Titanic",
                "genre": "Romance",
                "release_date": "November 18, 1997",
            },
        )
        movie = Movie.query.filter(Movie.title == "Titanic").first()

        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(movie)

    def test_add_new_movie_with_missing_fields(self):
        response = self.client.post(
            "/movies",
            headers=create_headers(EXECUTIVE_PRODUCER_TOKEN),
            json={"title": "Titanic_4", "release_date": ""},
        )
        movie = Movie.query.filter(Movie.title == "Titanic_4").first()

        self.assertEqual(response.status_code, 400)
        self.assertIsNone(movie)

    def test_add_new_actor(self):
        response = self.client.post(
            "/actors",
            headers=create_headers(EXECUTIVE_PRODUCER_TOKEN),
            json={
                "name": "John Doe",
                "gender": "Male",
                "age": 46,
            },
        )
        actor = Actor.query.filter(Actor.name == "John Doe").first()

        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(actor)

    def test_add_new_actor_with_missing_fields(self):
        response = self.client.post(
            "/actors",
            headers=create_headers(EXECUTIVE_PRODUCER_TOKEN),
            json={"title": "First Last", "gender": ""},
        )
        actor = Actor.query.filter(Actor.name == "First Last").first()

        self.assertEqual(response.status_code, 400)
        self.assertIsNone(actor)

    def test_delete_existing_movie(self):
        # Arrange
        Movie(id=9912, title="Titanic", genre="Romance",
              release_date=datetime.now()).insert()
        # Act
        response = self.client.delete(
            "/movies/9912",
            headers=create_headers(EXECUTIVE_PRODUCER_TOKEN),
        )

        # Assert
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(Movie.query.get(9912))

    def test_delete_non_existing_movie(self):
        response = self.client.delete(
            "/movies/991250",
            headers=create_headers(EXECUTIVE_PRODUCER_TOKEN),
        )

        self.assertEqual(response.status_code, 404)
        self.assertIsNone(Movie.query.get(99125))

    def test_delete_existing_actor(self):
        # Arrange
        Actor(id=9912, name="Noor", age=21, gender="Male").insert()
        # Act
        response = self.client.delete(
            "/actors/9912",
            headers=create_headers(EXECUTIVE_PRODUCER_TOKEN),
        )
        # Assert
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(Actor.query.get(9912))

    def test_delete_non_existing_actor(self):
        response = self.client.delete(
            "/actors/991235",
            headers=create_headers(EXECUTIVE_PRODUCER_TOKEN),
        )

        self.assertEqual(response.status_code, 404)
        self.assertIsNone(Actor.query.get(99125))

    def test_update_movie(self):
        # Arrange
        Movie(id=9912, title="Titanic", genre="Romance",
              release_date=datetime.now()).insert()
        # Act
        response = self.client.patch(
            "/movies/9912",
            headers=create_headers(EXECUTIVE_PRODUCER_TOKEN),
            json={"title": "The Shawshink Redemption"},
        )
        # Assert
        test_movie = Movie.query.get(9912)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(test_movie.title, "The Shawshink Redemption")
        # Clean up
        test_movie.delete()

    def test_update_movie_unprocessable_date(self):
        # Arrange
        Movie(id=9912, title="Titanic", genre="Romance",
              release_date=datetime.now()).insert()
        # Act
        response = self.client.patch(
            "/movies/9912",
            headers=create_headers(EXECUTIVE_PRODUCER_TOKEN),
            json={"title": 50, "release_date": "Not a date"},
        )
        # Assert
        test_movie = Movie.query.get(9912)
        self.assertEqual(response.status_code, 422)
        self.assertEqual(test_movie.title, "Titanic")
        # Clean up
        test_movie.delete()

    def test_update_actor(self):
        # Arrange
        Actor(id=9912, name="Noor", age=21, gender="Male").insert()
        # Act
        response = self.client.patch(
            "/actors/9912",
            headers=create_headers(EXECUTIVE_PRODUCER_TOKEN),
            json={"name": "Noor Salah", "age": 46},
        )
        # Assert
        test_actor = Actor.query.get(9912)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(test_actor.name, "Noor Salah")
        self.assertEqual(test_actor.age, 46)
        # Clean up
        test_actor.delete()

    def test_update_actor_unprocessable_date(self):
        # Arrange
        Actor(id=9912, name="Noor", age=21, gender="Male").insert()
        # Act
        response = self.client.patch(
            "/actors/9912",
            headers=create_headers(EXECUTIVE_PRODUCER_TOKEN),
            json={
                "name": 1232,
                "age": "Not a number",
                "gender": "Not a gender"},
        )
        # Assert
        test_actor = Actor.query.get(9912)
        self.assertEqual(response.status_code, 422)
        self.assertEqual(test_actor.name, "Noor")
        self.assertEqual(test_actor.age, 21)
        self.assertEqual(test_actor.gender, "Male")
        # Clean up
        test_actor.delete()

    def test_add_actor_to_movie_cast(self):
        response = self.client.patch(
            "/movies/1/actors/1",
            headers=create_headers(EXECUTIVE_PRODUCER_TOKEN)
        )

        test_movie = Movie.query.get(1)
        test_actor = Actor.query.get(1)
        self.assertEqual(response.status_code, 204)
        self.assertIn(test_actor, test_movie.actors)
        self.assertIn(test_movie, test_actor.movies)

    def test_add_non_existing_actor_to_movie_cast(self):
        response = self.client.patch(
            "/movies/1/actors/9999232",
            headers=create_headers(EXECUTIVE_PRODUCER_TOKEN)
        )

        test_movie = Movie.query.get(1)
        test_actor = Actor.query.get(9999232)
        self.assertEqual(response.status_code, 404)
        self.assertNotIn(test_actor, test_movie.actors)

    def test_add_movie_to_actor_movies_list(self):
        response = self.client.patch(
            "/actors/1/movies/1",
            headers=create_headers(EXECUTIVE_PRODUCER_TOKEN)
        )

        test_actor = Actor.query.get(1)
        test_movie = Movie.query.get(1)
        self.assertEqual(response.status_code, 204)
        self.assertIn(test_movie, test_actor.movies)
        self.assertIn(test_actor, test_movie.actors)

    def test_add_non_existing_movie_to_non_existing_actor_list(self):
        response = self.client.patch(
            "/actors/999123/movies/9912312",
            headers=create_headers(EXECUTIVE_PRODUCER_TOKEN)
        )

        self.assertEqual(response.status_code, 404)

    def test_get_actor_unauthenticated(self):
        response = self.client.get("/actors")

        self.assertEqual(response.status_code, 401)

    def test_add_actor_unauthorized(self):
        response = self.client.post(
            "/actors",
            headers=create_headers(CASTING_ASSISTANT_TOKEN),
            json={
                "name": "John Doe",
                "gender": "Male",
                "age": 46,
            },
        )

        self.assertEqual(response.status_code, 403)

    def test_patch_actor_unauthorized(self):
        response = self.client.patch(
            "/movies/9912",
            headers=create_headers(CASTING_ASSISTANT_TOKEN),
            json={"title": "The Shawshink Redemption"},
        )
        self.assertEqual(response.status_code, 403)

    def test_create_movie_unauthorized(self):
        response = self.client.post(
            "/movies",
            headers=create_headers(CASTING_DIRECTOR_TOKEN),
            json={
                "title": "WILL_NOT_BE_ADDED",
                "genre": "Romance",
                "release_date": "November 18, 1997",
            },
        )
        movie = Movie.query.filter(Movie.title == "WILL_NOT_BE_ADDED").first()

        self.assertEqual(response.status_code, 403)
        self.assertIsNone(movie)

    def test_delete_movie_unauthorized(self):
        response = self.client.delete(
            "/movies/5",
            headers=create_headers(CASTING_DIRECTOR_TOKEN),
        )

        movie = Movie.query.get(5)
        self.assertEqual(response.status_code, 403)
        self.assertIsNotNone(movie)
