import json

def create_config_file(data):
    file_path = 'config.json'
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def generate_data(places_len, weapons_len):
    data = {}
    data['weapons'] = ['weapon_' + chr(97 + i) for i in range(weapons_len)]
    data['places'] = ['place_' + chr(97 + i) for i in range(places_len)]
    return data

def read_file():
    file_path = 'config.json'
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        weapons = data['weapons']
        places = data['places']
    return weapons, places

data = generate_data(20, 10)
create_config_file(data)
