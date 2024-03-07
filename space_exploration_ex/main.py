import random

import Spaceship
import space_game

events = ["Asteroid Field", "Space Pirates", "Alien Diplomacy" , "Black Hole"]

def pick_event():
    event = random.choice(events)
    return event
def handle_game():
    spaceship = Spaceship.Spaceship('A',100,100)
    game = space_game.Space_Exploration_game(spaceship)
    game.launching()
    game.explore_the_galaxy()
    while True:
        if spaceship.health <= 0:
            print("Spaceship destroyed. Game over.")
            break
        if spaceship.fuel <= 0:
            print("Spaceship fuel is over. Game over.")
            break
        event = pick_event()
        game.handle_space_events(event)

handle_game()

