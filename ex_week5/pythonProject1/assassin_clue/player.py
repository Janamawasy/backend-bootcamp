import random

class Player():
    def __init__(self, name, visited_places, favorite_weapons):
        self.name = name
        self.visited_places = visited_places
        self.favorite_weapons = favorite_weapons

    def visit_place(self, place):
        self.visited_places.append(place)

