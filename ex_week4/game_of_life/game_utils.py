
def valid_coordination(coordination, board_size):
    '''
        :param coordination: is row col in string
        :param board_size: the size of the board game
        :return: False if the coordination not valid
                row col - as numbers if they are valid values
    '''
    row_col = coordination.split(' ')
    if len(coordination.split(' ')) != 2:
        return False
    row, col = row_col
    if not row.isdigit() or not col.isdigit():
        return False
    row, col = int(row), int(col)
    if 0 <= row < board_size and 0 <= col < board_size:
        return row, col

def calculate_live_neighbors(row,col,board_game):
    '''
        for cell index
        :param row: num of the row index
        :param col: num of the column index
        :param board_game: the size of the board game
        :return: number of live neighbors (value == 1) around the index
    '''
    live_neighbors = 0
    for i in range(max(0, row - 1), min(len(board_game), row + 2)):
        for j in range(max(0, col - 1), min(len(board_game[0]), col + 2)):
            if (i, j) != (row, col) and board_game[i][j] == 1:
                live_neighbors += 1
    return live_neighbors

def live_cell_rules(live_neighbors):
    '''
        rules according to Conway's Game of Life (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
        :param live_neighbors: number of live neighbors
        :return: cell status ( 0 - dead / 1 - alive)
    '''
    if live_neighbors<2:
        print('underpopulation: cell dies')
        return 0
    if 2 <= live_neighbors <= 3:
        print('lives on to the next generation')
        return 1
    if live_neighbors > 3:
        print('overpopulation: cell dies')
        return 0

def dead_cell_rules(live_neighbors):
    '''
        rules according to Conway's Game of Life (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
        :param live_neighbors: number of live neighbors
        :return: cell status ( 0 - dead / 1 - alive)
    '''
    if live_neighbors == 3:
        print('reproduction: cell lives')
        return 1
    else:
        return 0

