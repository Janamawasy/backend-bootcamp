import game_utils
import tkinter as tk



class GameOfLife():
    '''
    nnnn
    '''
    def __init__(self, board_size, live_cells) -> None:
        '''
        :param board_size: size of the board game
        :param live_cells: list of coordination of live cells : ['1 2', '0 0'...]
        '''

        self.board_size = board_size
        self.live_cells = live_cells
        self.board_game = [[0 for i in range(self.board_size)] for j in range(self.board_size)]

    def __str__(self):
        board_str = ""
        for row in self.board_game:
            board_str += f'{row}\n'
        return board_str

    def create_board(self):
        ''' populate live cells in the board game '''
        for coordination in self.live_cells:
            if game_utils.valid_coordination(coordination, self.board_size):
                row, col = game_utils.valid_coordination(coordination, self.board_size)
                self.board_game[int(row)][int(col)] = 1
            else:
                print(f' cell coordination {coordination} not valid ')

    def simulate_round(self):
        '''
            simulate one round, if cell is 0 - cell alive , if 1 - cell dead
            cell status will change according to live_cell_rules and dead_cell_rules
        '''
        for row in range(len(self.board_game)):
            for col in range(len(self.board_game[row])):
                live_neighbors = game_utils.calculate_live_neighbors(row, col, self.board_game)
                if self.board_game[row][col] == 1:
                    self.board_game[row][col] = game_utils.live_cell_rules(live_neighbors)
                else:
                    self.board_game[row][col] = game_utils.dead_cell_rules(live_neighbors)

    # def GUI(self):
    #     # create root window
    #     root = tk.Tk()
    #     t = self.board_game(root)
    #     root.mainloop()


