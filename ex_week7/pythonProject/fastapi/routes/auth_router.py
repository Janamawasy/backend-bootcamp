from fastapi import APIRouter
import utils.auth_fns as auth_fns
import utils.db_funcs as db_fns
from models.auth_model import Auth_Model
router = APIRouter()

@router.post('/auth/sign_up')
def sign_up(body:Auth_Model):
    updated_db = auth_fns.prepare_new_user_data(body.password,body.username)
    db_fns.save_to_db(updated_db)
    auth_token = auth_fns.generate_jwt({"user role":"guest"})
    return {"msg":"user created","token":auth_token}

@router.post('/auth/sign_in')
def sign_in(body:Auth_Model):
    try:
        stored_user = db_fns.find_user_in_db(body.username)
        if stored_user:
            stored_pass = stored_user["password"]
            if auth_fns.verify_password(stored_pass,body.password):
                auth_token = auth_fns.generate_jwt({"user role":"guest"})
                return {"msg":"user sign in successfully","token":auth_token}
            else:
                return {"msg":"invalid creds"}
    except Exception as e:
        print(e)
        return {"msg": "no such username"}