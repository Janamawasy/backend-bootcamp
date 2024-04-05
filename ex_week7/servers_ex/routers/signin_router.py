from fastapi import APIRouter
from classes.user_class import User
from utils.user_funcs import check_user
from auth.jwt_handler import sign_jwt

router = APIRouter()

@router.post("/sign-in")
async def log_in(user: User):
    """
    function logging in and creating tokens
    :param user: User class obj, has username, password and role
    :return: if success return: {"access token": token} if fail will return {"error": "Invalid login details"}
    """
    if check_user(user.username, user.password):
        return sign_jwt(user.username)
    else:
        return {
            "error": "Invalid login details"
        }
