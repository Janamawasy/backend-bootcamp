import json

def create_config_file(data):
    '''
    Creates a JSON configuration file with the provided data.
    :param data: data (dict): The data to be written to the JSON file
    :return: None
    '''
    file_path = 'config.json'
    try:
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
    except IOError as e:
        print(f"Error creating config file: {e}")
        raise


def generate_data(places_len, weapons_len):
    '''
     Generates sample data for weapons and places.
    :param places_len: number of places to generate
    :param weapons_len: number of weapons to generate
    :return: dict: A dictionary containing generated data for weapons and places
    '''
    data = {}
    data['weapons'] = ['weapon_' + chr(97 + i) for i in range(weapons_len)]
    data['places'] = ['place_' + chr(97 + i) for i in range(places_len)]
    return data

def read_file():
    '''
    Reads weapons and places from the config file.
    :return: list of weapons and list of places
    '''
    file_path = 'config.json'
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            weapons = data['weapons']
            places = data['places']
        return weapons, places
    except FileNotFoundError as e:
        print(f"Config file not found: {e}")
        raise
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        raise

# data = generate_data(20, 10)
# create_config_file(data)
