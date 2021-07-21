import json
import os
from flask import request
from functools import wraps
from jose import jwt
from urllib.request import urlopen
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
API_AUDIENCE = os.getenv("API_AUDIENCE")
ALGORITHMS = ["RS256"]


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


def get_token_auth_header():
    auth_header = request.headers.get("Authorization", None)
    if auth_header is None:
        raise AuthError("Authorization header is missing", 401)
    header_parts = auth_header.split()
    if header_parts[0].lower() != "bearer":
        raise AuthError("Invalid Header: must start with Bearer.", 401)
    if len(header_parts) == 1:
        raise AuthError("Invalid Header: Missing token", 401)
    if len(header_parts) > 2:
        raise AuthError("Invalid Header: Must be bearer token", 401)
    jwt_token = header_parts[1]
    return jwt_token


def check_permissions(permission, payload):
    permissions = payload.get("permissions", None)
    if permissions is None:
        raise AuthError("Bad request: No permissions exist", 400)
    if permission not in permissions:
        raise AuthError("Unauthorized request", 403)
    return True


def verify_decode_jwt(token):
    jsonurl = urlopen(f"https://{AUTH0_DOMAIN}/.well-known/jwks.json")
    jwks = json.loads(jsonurl.read())
    unverified_header = jwt.get_unverified_header(token)
    rsa_key = {}
    if "kid" not in unverified_header:
        raise AuthError("Invalid Header: Authorization malformed.", 401)

    for key in jwks["keys"]:
        if key["kid"] == unverified_header["kid"]:
            rsa_key = {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"],
            }
    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer="https://" + AUTH0_DOMAIN + "/",
            )

            return payload

        except jwt.ExpiredSignatureError:
            raise AuthError("Error: Token Expired", 401)

        except jwt.JWTClaimsError:
            raise AuthError(
                "Invalid claims: Please check the audience and the issuer.", 401
            )
        except Exception:
            raise AuthError("Invalid Header: Unable to parse authentication token", 400)
    raise AuthError("Invalid Header: Unable to find the appropriate key.", 400)


def requires_auth(permission=""):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            payload = verify_decode_jwt(token)
            check_permissions(permission, payload)
            return f(payload, *args, **kwargs)

        return wrapper

    return requires_auth_decorator
