import random

class Game():
    def __init__(self):
        self.players = []
        self.assassin_name = ''
        self.crime_place = ''
        self.crime_weapon = ''
        pass

    def add_player(self, player):
        '''
        :param player: player instance
        :return: None
        '''
        self.players.append(player)
        print('player added successfully')

    def choose_assassin(self)->None:
        '''
        the function choose assassin randomly and update crime_weapon
        :return: None
        '''
        if not self.players:
            raise ValueError("No players added to the game.")
        assassin = random.choice(self.players)
        self.assassin_name = assassin.name

        self.crime_weapon = assassin.favorite_weapons[-1]
        print(f'assassin is: {assassin.name}')

    def murder(self) -> None:
        '''
        function apply the murder by choosing victim from players without the assassin and update crime_place
        :return:
        '''
        if not self.players:
            raise ValueError("No players left in the game.")
        other_players = [player for player in self.players if player.name != self.assassin_name]
        if not other_players:
            raise ValueError("No potential victims left")
        victim = random.choice(other_players)
        print(f'{victim.name} is dead')
        crime_seen = victim.visited_places[0]
        for p in self.players:
            if p.name == self.assassin_name:
                p.visited_places.append(crime_seen)
                self.crime_place = crime_seen
        self.players.remove(victim)

    def player_suspect(self, player) -> bool:
        '''
        the function choose and print suspects randomly and choose player to accuse
        :param player: player instance to choose suspects
        :return: True : game over, False: the assassin still in the game
        '''
        if len(self.players) < 3:
            raise ValueError("Not enough players remaining in the game.")
        other_players = [p for p in self.players if p != player]
        suspects = random.sample(other_players, 2)
        for suspect in suspects:
            print(f'suspect: {suspect.name} visited placed- {suspect.visited_places[0]} and {suspect.visited_places[-1]} , favorite weapon- {suspect.favorite_weapons[0]}' )
        final_suspect = random.choice(suspects)
        print(f'accused player : {final_suspect.name}')
        res = self.accuse_player(final_suspect)
        return res

    def accuse_player(self, final_suspect) -> bool:
        '''
        the function chick the accusation
        :param final_suspect: suspect instance
        :return: True : game over, False: the assassin still in the game
        '''
        if final_suspect.name == self.assassin_name:
            print(f'murderer founded :{final_suspect.name} - game over')
            return True
        else:
            print(f'{final_suspect.name} is not the murderer.')
            return False

        def manage_rounds(self):
        '''
        run rounds until finding the assassin or no players left in the game
        '''
        try:
            while len(self.players) > 2:
                print('****************************')
                self.murder()
                for player in self.players:
                    res = self.player_suspect(player)
                    if res:
                        break
                else:  # This else block executes if the inner loop completes without breaking
                    continue  # Continue with the next iteration of the outer loop if no accusation was successful
                break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")




