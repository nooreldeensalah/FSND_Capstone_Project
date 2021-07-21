# Udacity Casting Agency (Capstone Project)

Udacity Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies.

## Local Setup
To get the project working locally, you will need to create a virtual environment.
```
python -m venv venv
```
Then activate the virtual environment depending on your operating system.
Windows `./venv/Scripts/activate`
Linux/macOS `source venv/bin/activate`

Install the required packages `pip install -r requirements.txt`

Export the required environment variables by running one of the following scripts, depending on your shell choice:
- `setup.sh`  (Bash).
- `setup.ps1` (PowerShell).
- `setup.bat` (Command Prompt).
 
 
The project uses two local databases:
- `CastingAgencyDB` which is the main database that runs the application.
- `TestCastingAgencyDB` which is a database used for testing purposes.

Create tables and seed the databases by running these commands
```
createdb CastingAgencyDB
createdb TestCastingAgencyDB
psql CastingAgencyDB < seed.sql
psql TestCastingAgencyDB < seed.sql
```
*Note*: Windows users might have to provide a user/password when running PostgreSQL system commands, example:
`createdb -U postgres CastingAgencyDB`

Start the flask application by running the command `flask run`
 (*Note*: You don't need to set `FLASK_APP` In case you executed one of the scripts mentioned above).

# Testing

The project contains two test suites:
- RBAC tests in the postman collection `Casting Agency.postman_collection.json`
- API Endpoints tests in `test_app.py`

To run the RBAC tests, just import the collection in [Postman](https://www.postman.com/) and run it (make sure the application is running).
 To run the  API endpoints tests in `test_app.py` You can run either of those commands:
- `python -m unittest` 
- `pytest`  (requires `pytest` to be installed).

# Authentication (Using Auth0)
Udacity Casting Agency has 3 roles:
- **Casting Assistant**
	- Permissions
		- `get:movies`
		- `get:actors`
	- Auth0 login data
		- ID: `casting_assistant@example.com`
		- Password:`5e.*shwR\AdgzBkf`
- **Casting Director**
	 - Permissions
		- `get:movies`
		- `get:actors`
		- `patch:actors`
		- `patch:movies`
		- `post:actors`
		- `delete:actors`
	- Auth0 login data
		- ID: `casting_director@example.com`
		- Password:`5e.*shwR\AdgzBkf`
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
	- Auth0 login data
		- ID: `executive_producer@example.com`
		- Password:`5e.*shwR\AdgzBkf`


# API Documentation

ENDPOINT

Example Request
```
```

Example Response
```
```