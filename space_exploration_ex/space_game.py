import time
import random
import json
import math
import requests

class Space_Exploration_game():
    def __init__(self, spaceship):
        print(str(spaceship))
        self.time = time.monotonic()
        self.spaceship = spaceship

    def launching(self):
        self.update_time()
        self.spaceship.fuel = 0.8 * self.spaceship.fuel
        self.spaceship.health -= 0.1 * self.spaceship.health
        print(str(self.spaceship))

    def update_time(self):
        current_time = time.monotonic()
        diff_time = current_time - self.time
        self.time = current_time
        return diff_time

    def explore_the_galaxy(self):
        diff_time = self.update_time()
        self.calculate_fuel(diff_time)

    def handle_space_events(self, event):
        diff_time = self.update_time()
        self.calculate_fuel(diff_time)
        match event:
            case 'Asteroid Field':
                print('mode: fire at the asteroids ')
                self.spaceship.fuel = 0.5 * self.spaceship.fuel
            case "Space Pirates":
                print('mode: run away!')
                self.spaceship.fuel = 0.6 * self.spaceship.fuel
                self.spaceship.health = 0.6 * self.spaceship.health
            case "Alien Diplomacy":
                print('mode: negotiation')
            case "Black Hole":
                print('mode: Game Over')
                self.spaceship.health = 0
        print(str(self.spaceship))

    def calculate_fuel(self, diff_time):
        self.spaceship.fuel = (1 - diff_time) / 1000 * self.spaceship.fuel
        return str(self.spaceship)

    def fetch_weather_data(self):
        pass

    def save_data(self):
        pass

    def load_data(self):
        pass