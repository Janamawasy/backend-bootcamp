import validate_inputs
import logging

def manage_cli():
    logging.info("Game started")
    board_size = validate_inputs.valid_number('choose the size of the board game : ')
    print('choose live cells, when you finish choosing Press Enter')
    choices = []
    while True:
        choice = input('Enter live cell (row, column) separated with space: ')
        if choice == '':
            break
        choices.append(choice)
    rounds = validate_inputs.valid_number('how many round would you like? ')
    return board_size, rounds, choices
