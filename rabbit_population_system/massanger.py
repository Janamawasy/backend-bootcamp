class Massanger():

    def __init__(self):
        self.last_record_index = 0

    def update_record_index(self, last_index):
        self.last_record_index = last_index
        print('update: ',self.last_record_index)

    def get_record_index(self):
        print('get :',self.last_record_index)
        return self.last_record_index



# class Store:
#     def __init__(self):
#         self.last_record_index = 0
#
#     def dispatch(self, action):
#         if action['type'] == 'SAVE_RECORD_INDEX':
#             self.last_record_index = action['payload']
#         elif action['type'] == 'GET_LAST_INDEX':
#             return self.last_record_index
#         return None
#
# # Actions
# def save_record_index(index):
#     return {'type': 'SAVE_RECORD_INDEX', 'payload': index}
#
# def get_last_index():
#     return {'type': 'GET_LAST_INDEX'}
#
# # Reducer
# def reducer(state, action):
#     return state.dispatch(action)



#
# def massanger(msg,last_index = None):
#     last_record_index = 0
#     match msg:
#         case 'save_record_index':
#             last_record_index = last_index
#         case 'get_last_index':
#             return last_record_index
#     print('aaaaa',last_record_index)
#
# msngr = Massanger()
