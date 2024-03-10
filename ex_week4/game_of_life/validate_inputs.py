
def valid_number(inpur_text):
    while True:
        num = input(inpur_text)
        if num.isdigit():
            break
    return int(num)


def valid_choice(choice, board_size):
    row_col = choice.split(' ')
    if len(choice.split(' ')) != 2:
        return False
    row, col = row_col
    if not row.isdigit() or not col.isdigit():
        return False
    row, col = int(row), int(col)
    if 0 <= row < board_size and 0 <= col < board_size:
        return row, col



