import bcrypt
from utils.data_funcs import read_db

def password_hashing(password):
    '''
    hashing and salting password with bcrypt
    :param password: real password
    :return: hashed password
    '''
    # Adding the salt to password
    salt = bcrypt.gensalt()
    password_bytes = password.encode()
    # Hashing the password
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed


def check_user(username, password):
    '''
    checking if username and password are correct and exist in users database
    :param username: username
    :param password: password
    :return: bool
    '''
    filename = 'data/users_data.json'
    users = read_db(filename)
    if username in users:
        hashed_password = users[username]["password"]
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
            return True
        else:
            return False
    else:
        return False


