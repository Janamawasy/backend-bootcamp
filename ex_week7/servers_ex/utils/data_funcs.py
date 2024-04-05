import json


def read_db(filename):
    '''
    getting data from file
    :param filename: file directory
    :return: database
    '''
    try:
        with open(filename, 'r') as f:
            # file_content = f.read()
            # # print("File content:", file_content)
            # db = json.loads(file_content)
            db = json.load(f)
            return db
    except Exception as e:
        print("Error reading file:", e)
        return {}

def save_user_db(db, filename):
    '''
    add new data to file and manipulate hashed data format
    :param db: new data to be added
    :param filename: filename directory
    :return: bool
    '''
    try:
        # Convert bytes passwords to strings
        for username, userdata in db.items():
            if 'password' in userdata and isinstance(userdata['password'], bytes):
                userdata['password'] = userdata['password'].decode('utf-8')

        with open(filename, 'w') as f:
            json.dump(db, f, indent=4)
        print('in save db')
        return True
    except Exception as e:
        print('Error in saving data', e)
        return False

def save_db(db, filename):
    '''
    add new data to file
    :param db: new data to be added
    :param filename: filename directory
    :return: bool
    '''
    try:
        with open(filename, 'w') as f:
            json.dump(db, f, indent=4)
        return True
    except Exception as e:
        print('Error in saving data', e)
        return False



