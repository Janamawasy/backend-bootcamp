from fastapi.security import HTTPAuthorizationCredentials, HTTPBasic
from fastapi import Depends, HTTPException
from utils.data_funcs import read_db
from utils.user_funcs import check_user
from auth.jwt_bearer import jwtBearer
from auth.jwt_handler import decodeJWT
import jwt
from decouple import config
from fastapi import Depends, FastAPI, HTTPException, Header


JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

# Define the security instance
security = HTTPBasic()
# def is_admin(credentials: HTTPAuthorizationCredentials = Depends(security)):
#     user_db = read_db('data/users_data.json')
#     user = user_db[credentials.username]
#     if not user:
#         raise HTTPException(status_code=401, detail="Invalid username or password")
#     if user["role"] != "admin":
#         raise HTTPException(status_code=403, detail="User is not an admin")
#     print('is admin')
#     return user

# def is_admin(jwtoken: str = Depends(jwtBearer())):
#     payload = decodeJWT(jwtoken)
#     print('role:', payload)
#     if not payload or payload.get("role") != "admin":
#         raise HTTPException(status_code=403, detail="User is not an admin")
#     return True

def get_token(authorization: str = Header(None)):
    if authorization is None:
        raise HTTPException(status_code=401, detail="Authorization header is missing")
    parts = authorization.split()
    if len(parts) != 2 or parts[0].lower() != "bearer":
        raise HTTPException(status_code=401, detail="Invalid authorization header")
    return parts[1]

def is_admin(jwtoken: str = Depends(get_token)):
    try:
        payload = jwt.decode(jwtoken, JWT_SECRET, algorithms=["HS256"])
        role = payload.get("role")
        return role == "admin"
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")



# admin permition did not work succesfully!
