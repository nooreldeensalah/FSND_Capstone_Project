import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
CONNECTION_STRING = os.getenv("DB_CONNECTION_STRING")

db = SQLAlchemy()


# There are two databases created.
# 1) CastingAgencyDB (Default Database).
# 2) TestCastingAgencyDB (Used for testing).
def setup_db(app, connection_string=CONNECTION_STRING):
    app.config["SQLALCHEMY_DATABASE_URI"] = connection_string
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = os.urandom(32)
    db.app = app
    db.init_app(app)


association_table = db.Table(
    "movie_actor",
    db.Column("movie_id", db.Integer, db.ForeignKey("movie.id"), primary_key=True),
    db.Column("actor_id", db.Integer, db.ForeignKey("actor.id"), primary_key=True),
)


class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    release_date = db.Column(db.DateTime, nullable=False)
    genre = db.Column(db.String(80), nullable=False)
    actors = db.relationship("Actor", secondary="movie_actor", backref="movies")

    def add_actor(self, actor):
        if actor not in self.actors:
            self.actors.append(actor)
        db.session.commit()

    def insert(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def update():
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "id": self.id,
            "title": self.title,
            "genre": self.genre,
            "release_date": self.release_date.strftime("%B %d, %Y"),
            "actors": [actor.name for actor in self.actors],
        }

    def __repr__(self):
        return f"Movie(title={self.title}, genre={self.genre}, release_date={self.release_date.strftime('%B %d, %Y')})"


class Actor(db.Model):
    __tablename__ = "actor"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Enum("Male", "Female", name="gender"), nullable=False)

    def add_movie(self, movie):
        if movie not in self.movies:
            self.movies.append(movie)
        db.session.commit()

    def insert(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def update():
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "movies": [movie.title for movie in self.movies],
        }

    def __repr__(self):
        return f"Actor(name={self.name}, age={self.age}, gender={self.gender})"
