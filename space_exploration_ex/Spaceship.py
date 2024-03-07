class Spaceship():
    def __init__(self, name, fuel, health):
        self.name = name
        self.fuel = fuel
        self.health = health

    def __str__(self):
        return f' spaceship name : {self.name}, fuel: {self.fuel}, health: {self.health}'