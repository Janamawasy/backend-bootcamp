# this file is responsible for signing in, encoding, decoding and returning JWT

import time
import jwt
from decouple import config

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

# Function returns generated tokens
def token_response(token: str):
    return {
        "access token": token
    }

# Function signing the JWT string
def sign_jwt(userID: str):
    payload = {
        "userID": userID,
        "expiry": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)

def decodeJWT(token: str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
        if decode_token['expiry'] >= time.time():
            return decode_token
        else:
            return None
    except:
        return {}
