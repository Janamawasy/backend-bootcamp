from fastapi import APIRouter
from classes.user_class import User
from utils.user_funcs import password_hashing
from utils.data_funcs import read_db, save_user_db
from auth.jwt_handler import sign_jwt

router = APIRouter()
@router.post("/sign-up")
async def registration(user: User):
    '''
    create new user, add it to users db json file with hashed password
    :param user: User class obj, has username, password and role
    :return: if success return: {'massage': 'success', "token": token} if fail will return {'massage': 'fail'}
    '''
    hashed_pass = password_hashing(user.password)
    print('hashed_pass', hashed_pass)
    # hashed_pass = user.password

    filename = 'data/users_data.json'
    users_data = await read_db(filename)
    print('users_data', users_data)
    if user.username in users_data:
        print('user already exist!')
    else:
        userdata = {
            "username": user.username,
            "password": hashed_pass,
            "role": user.role
        }
        users_data[user.username] = userdata
        print('users_data', users_data)
        res = save_user_db(users_data, filename)
        token = sign_jwt(user.username)
        if res:
            return {'massage': 'success', "token": token}
        else:
            return {'massage': 'fail'}


# post req:
# Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/sign-up -Body '{"username":"user1","password":"123"}' -ContentType "application/json"