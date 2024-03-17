import random
import handle_file
import player
import game

def start_the_game(num_of_players:int) -> None:
    '''
    the function add the players to the game
    :param num_of_players: number of players in the game
    :return:
    '''
    for i in range(num_of_players):
        num_of_places = random.randint(1, 5)
        p = player.Player('player_'+chr(97+i), random.sample(places,num_of_places), random.sample(weapons,2))
        game.add_player(p)


if __name__ == "__main__":
    try:
        weapons, places = handle_file.read_file()
        num_of_players = 10  # Adjust the number of players as needed
        if not 2 < num_of_players <= len(places):  # Adjust the range of valid number of players
            raise ValueError("Invalid number of players.")
        if not num_of_players.isdigit():
            raise TypeError("Invalid type input")
        else:
            num_of_players = int(num_of_players)
        game = game.Game()
        start_the_game(num_of_players)
        game.choose_assassin()
        game.manage_rounds()

    except FileNotFoundError:
        print("File not found.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

