import json
from json_interactor import raise_random_exception_with_probability



class Analyzer():
    def __init__(self, current_alive_rabbits, massanger):
        self.massanger = massanger
        self.current_alive_rabbits = current_alive_rabbits
        self.last_record = 0
        self.records = []
        pass

    def get_records(self):
        '''
        read data-> find self.last_record -> store 10 records after self.last_record
        '''
        self.records = []
        # all_data = get_data()
        all_data = raise_random_exception_with_probability(self.get_data)
        new_record_index = int(self.last_record) + 1
        len_all_data = len(all_data)
        for i in range(10):
            if new_record_index + i < len_all_data:
                self.records.append(all_data[new_record_index + i])
                # self.last_record = new_record_index + i
                a = new_record_index + i
            else:
                a = new_record_index
        self.last_record = a
        print('mm',self.records)

    def update_rabbits_num(self):
        for record in self.records:
            for id, value in record.items():
                if self.validate_record(value):
                    self.current_alive_rabbits += value['birth_num'] - value['death_num']
        print('rabbits alive: ',self.current_alive_rabbits)

    def validate_record(self, record)->bool:
        print(record)
        print(self.current_alive_rabbits)
        if record['death_num'] > self.current_alive_rabbits:
            return False
        else:
            return True

    def manage_analyzer(self):
        # last_insert = massanger.massanger('get_last_index')
        last_insert = self.massanger.get_record_index()
        print(last_insert)
        while self.last_record < int(last_insert):
            self.get_records()
            self.update_rabbits_num()

    def get_data(self):
        try:
            with open('data/records.json', 'r') as file:
                file_data = json.load(file)
                return file_data
        except Exception:
            print('error: ', Exception)


# analyzer1 = Analyzer(100)
# analyzer1.manage_analyzer()
