import interface
import game
import tkinter as tk
import logging


def main():
    '''
    :return: board game matrix after each round
    '''
    size, rounds, live_cells = interface.manage_cli()
    logging.info(f"Received input: Size={size}, Rounds={rounds}, Live cells={live_cells}")
    game_of_life = game.GameOfLife(size, live_cells)
    game_of_life.create_board()
    logging.info("Game board created")
    print(str(game_of_life))
    logging.info("Starting simulation")
    for _ in range(rounds):
        game_of_life.simulate_round()
        logging.info("Round simulation completed!")
        print(str(game_of_life))
    logging.info("Game simulation completed!")


if __name__ == "__main__":
    # tk.Tk().mainloop()
    main()


