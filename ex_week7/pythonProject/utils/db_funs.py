import json


async def read_db(filename):
    with open(filename, 'r') as f:
        db = json.load(f)
    return db

def save_db(db, filename):
    with open(filename, 'w') as f:
        f.write(db)
