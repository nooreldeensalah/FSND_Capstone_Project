# Udacity Casting Agency (FSND Capstone Project)

Udacity Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies.

## Motivation
I developed this project to practice and solidify the concepts I've learned in Udacity's Full Stack Web Developer Nanodegree.

The topics include but are not limited to:
- Relational Database Architecture Modeling with PostgreSQL and SQLAlchemy.
- HTTP Protocol and Methods.
- API Development with Flask.
- Authentication and Authorization using third-party services such as **Auth0**
- Role-Based Access Control in Flask.
- Application Deployment using Hosting Services such as **AWS** or **Heroku**

## API Technology Stack and package dependencies
The technology stack and required packages can be found in `requirements.txt`, but most notable dependencies are:
- Python 3.7+
- PostgreSQL Server Database.
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-CORS
- python-dotenv

## Remote Setup
The live application is hosted on [https://aqueous-eyrie-91349.herokuapp.com/](https://aqueous-eyrie-91349.herokuapp.com/)
### Deployment Instructions

- Create an applicaton using Heroku's CLI
```
heroku create <app_name>
```
- Add PostgreSQL Server Add-on to the application.
```
heroku addons:create heroku-postgresql:hobby-dev --app <app_name>
```
- Configure Config Variables through Application Dashboard on Heroku.

- Deploy the application with Heroku
```
git push heroku main
```
- Apply database migrations.
```
heroku run python manage.py db upgrade --app <app_name>
```
- Establish a psql session with the remote database
```
heroku pg:psql
```
- Apply a script to seed the database
```
\i seed_after_migration.sql
```
You can now exist and test the application endpoints.
## Local Setup
To get the project working locally, you will need to create a virtual environment.
```
python -m venv venv
```
Then activate the virtual environment depending on your operating system.

Windows `./venv/Scripts/activate`

Linux/macOS `source venv/bin/activate`

Install the required packages `pip install -r requirements.txt`

The project uses two local databases:
- `CastingAgencyDB` which is the main database that runs the application.
- `TestCastingAgencyDB` which is a database used for testing purposes.

Create the tables.
```
createdb CastingAgencyDB
createdb TestCastingAgencyDB
```

Apply database migrations to create tables`python manage.py db upgrade
`  *Note*: Migrations are only applied on `CastingAgencyDB`

**Seeding the database**

- The migrations are only applied to `CastingAgencyDB` database, after applying the migrations you can run `psql CastingAgencyDB <  seed_after_migration.sql`
- Since migrations aren't applied on the testing database, no tables are created, thus we can create the tables and seed the database by running a different SQL script that creates the tables before seeding: `psql TestCastingAgencyDB < seed_for_testing.sql` 

Start the flask application by running the command `flask run`

## Testing

The project contains two test suites:
- RBAC tests in the postman collection `Casting Agency.postman_collection.json` (Remote testing by default, unless **host** variable is changed in the collection to localhost:5000)
- API Endpoints tests in `test_app.py`

To run the RBAC tests, just import the collection in [Postman](https://www.postman.com/) and run it.

**Note**: The delete test on Postman isn't idempotent, i.e. an item can only be deleted once then the test will fail, unless the *<item_id>* is changed.

 To run the  API endpoints tests in `test_app.py` You can run either of those commands:
- `python -m unittest` 
- `pytest`  (requires `pytest` to be installed).

## Authentication (Using Auth0)
Udacity Casting Agency has 3 roles:
- **Casting Assistant**
	- Permissions
		- `get:movies`
		- `get:actors`
- **Casting Director**
	 - Permissions
		- `get:movies`
		- `get:actors`
		- `patch:actors`
		- `patch:movies`
		- `post:actors`
		- `delete:actors`
- **Executive Producer**
	 - Permissions
		- `get:movies`
		- `get:actors`
		- `patch:actors`
		- `patch:movies`
		- `post:actors`
		- `delete:actors`
		- `post:movies`
		- `delete:movies`
	
## API Documentation

### Endpoints
- GET /movies
- GET /actors
- POST /movies
- POST /actors
- PATCH /movies/<movie_id>
- PATCH /actors/<actor_id>
- DELETE /movies/<movie_id>
- DELETE /actors/<actor_id>
- PATCH /movies/<movie_id>/actors/<actor_id>
- PATCH /actors/<actor_id>/movies/<movie_id>
---
**API Status codes**
- `200` Indicates a successful GET request.
- `201` Indicates a successful POST request.
- `204` Indicates a successful DELETE or PATCH request.
- `401` Indicates an authorized request, with no authorization header or invalid token.
- `403` Indicates an authorized request with insufficient permissions.
- `404` Indicates a non-existing resource in DELETE, GET, and PATCH requests.
- `405` Indicates a not allowed method.

Error handler JSON format
```
{"error": error.code, "message": error.description}
```
Example:
```json
{
    "error": 401,
    "message": "Authorization header is missing"
}
```
-----

**GET /movies**  
Retrieves a page of movies, optional arguments include page number and number of movies per page (limit).
  
Example Request  
```http
curl localhost:5000/movies?page=1&limit=3
```  
  
Example Response  
```json
{
    "movies": [
        {
            "actors": [],
            "genre": "Comedy|Crime|Thriller",
            "id": 1,
            "release_date": "March 11, 1998",
            "title": "Aankhen"
        },
        {
            "actors": [],
            "genre": "Drama",
            "id": 2,
            "release_date": "May 02, 2007",
            "title": "Prime of Miss Jean Brodie, The"
        },
        {
            "actors": [
                "Erma Rolfe"
            ],
            "genre": "Drama|Horror",
            "id": 3,
            "release_date": "October 17, 2008",
            "title": "Beyond Bedlam"
        }
    ]
}
```


**GET /actors**
Retrieves a page of actors, optional arguments include page number and number of actors per page (limit).

Example Request
```
curl localhost:5000/actors?page=1&limit=3
```
Example Response
```json
{
    "actors": [
        {
            "age": 39,
            "gender": "Female",
            "id": 2,
            "movies": [
                "How Tasty Was My Little Frenchman (Como Era Gostoso o Meu FrancÃªs)"
            ],
            "name": "Quincey Mahomet"
        },
        {
            "age": 75,
            "gender": "Male",
            "id": 3,
            "movies": [
                "Iron Island (Jazireh Ahani)"
            ],
            "name": "Merrile Aaronsohn"
        },
        {
            "age": 64,
            "gender": "Female",
            "id": 4,
            "movies": [
                "How Tasty Was My Little Frenchman (Como Era Gostoso o Meu FrancÃªs)"
            ],
            "name": "Everard Winsom"
        }
    ]
}
```

**POST /movies**
Add a new movie to the database.
Example Request
```
curl -X POST -H "Content-Type: application/json"
-d '{

"title":  "The Shawshink Redemption",

"release_date":  "September 10, 1994",

"genre":  "Prison|Drama|Crime Fiction"

}' localhost:5000/movies
```
Example Response
```
None
```

**POST /actors**
Add a new actor to the database.
Example Request
```
curl -X POST -H "Content-Type: application/json"
-d '{

"name":  "Morgan Freeman",

"age":  84,

"gender":  "Male"

}' localhost:5000/actors
```
Example Response
```
None 
```
**PATCH /movies/<movie_id>**
Updates an existing movie data.
Example Request
```
curl -X PATCH -H "Content-Type: application/json"
-d '{"title":  "The Shawshink Redemption"}' localhost:5000/movies/1
```
Example Response
```
None
```
**PATCH /actors/<actor_id>**
Updates an existing actor data.
Example Request
```
curl -X PATCH -H "Content-Type: application/json"
-d '{"name":  "Tim Robbins"}' localhost:5000/actors/1
```
Example Response
```
None
```
**DELETE /movies/<movie_id>**
Deletes a movie from the database.

Example Request
```
curl -X DELETE localhost:5000/movies/1
```
Example Response
```
None
```

**DELETE /actors/<actor_id>**
Deletes an actor from the database.

Example Request
```
curl -X DELETE localhost:5000/actors/1
```
Example Response
```
None
```

**PATCH /movies/<movie_id>/actors/<actor_id>**
Adds an actor to a movie's cast.
Example Request
```
curl -X PATCH localhost:5000/movies/1/actors/1
```
Example Response
```
None
```

**PATCH /actors/<actor_id>/movies/<movie_id>**
Adds a movie to an actor's movies list.
```
curl -X PATCH localhost:5000/actors/1/movies/1
```
Example Response
```
None
```