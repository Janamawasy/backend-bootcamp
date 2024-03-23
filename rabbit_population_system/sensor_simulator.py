# data ->
# sensor
# backend

import json
import random
import time

from json_interactor import raise_random_exception_with_probability

def new_record():
    death_num = random.randint(1,20)
    birth_num = random.randint(1,20)
    record_time = time.time()
    record = {'record_time': record_time, 'death_num': death_num, 'birth_num': birth_num}
    return record

def store_recored(record, massanger):
    try:
        with open('./data/records.json', 'r') as file:
            file_data = json.load(file)
            if file_data:
                last_index = list(file_data[-1].keys())[0]
            else:
                file_data = []
                last_index = 0
    except (FileNotFoundError, json.JSONDecodeError):
        raise FileNotFoundError

    file_data.append({int(last_index) + 1:record})
    massanger.update_record_index(int(last_index) + 1)
    try:
        with open('./data/records.json', 'w') as file:
            json.dump(file_data, file, indent=4)
    except Exception:
        print('error', Exception)


def generate_records(num_of_records, massanger):
    for i in range(num_of_records):
        record = new_record()
        # store_recored(record,massanger)
        raise_random_exception_with_probability(store_recored,record,massanger)
        time.sleep(random.randint(5,10))

# generate_records(5)

# a = [{1: '23'}, {2: 'lkdms'}, {3: 'fds'}]
# print(list(a[-1].keys())[0])