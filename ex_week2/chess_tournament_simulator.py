import random

players = {}
# {1:{},2:{},,}
def create_player(name, rank, total):
    if len(players) > 0:
        id = max(players.keys())+1
    else:
        id = 1
    player = {'name' : name, 'rank' : [rank], 'total': total}
    players[id] = player

def simulate_round():
    sets = []
    for i in range(len(players)):
        for j in range(i, len(players)):
            if i != j:
                sets.append([i + 1, j + 1])
    return sets

def round_robin():
    # all players should face each other
    # output : 1 - win , 0.5 - draw, 0 - loss
    games = simulate_round()
    for [player1,player2] in games:
        calculate_game_winner(player1,player2)

    return winner()


def calculate_game_winner(player1, player2):
    # chance of winning for each player
    # 0.2 - draw
    # 0.8 = chance_1 + chance_2
    ratio = players[player1]['rank'][-1] / players[player2]['rank'][-1]
    revers_ratio = 1 - ratio
    chance_1 = 0.4 - revers_ratio
    chance_2 = 0.4 + revers_ratio
    draw = 0.2
    # print(player1, chance_1, player2, chance_2)
    if chance_1 is max(chance_1,chance_2,draw):
        add_points(player1, 1)
        update_elo_rating(player1, player2,1)
    if chance_2 is max(chance_1,chance_2,draw):
        add_points(player2, 1)
        update_elo_rating(player2,player1, 1)
    if draw is max(chance_1,chance_2,draw):
        add_points(player1, 0.5)
        add_points(player2, 0.5)
        update_elo_rating(player1, player2,0.5)
        update_elo_rating(player2, player1, 0.5)

def add_points(player, points):
    players[player]['total'] += points

def winner():
    max_total = 0
    max_player = ''
    winner_player = {}
    for player_id, player in players.items():
        if player['total'] > max_total:
            max_total = player['total']
            max_player = player['name']
            winner_player = player
    print(f'the winner is {max_player} with {max_total} total points')
    print(f'winner : {winner_player}')
def update_elo_rating(winner_num, opponent, points):
    # the weaker wins
    if players[opponent]['rank'][-1] > players[winner_num]['rank'][-1]:
        K = 32
    # if the stronger wins or they have the same strength
    else:
        K = 16
    # new_rate = rate + K * (new_score - score)
    new_rank = players[winner_num]['rank'][-1] + K * points
    players[winner_num]['rank'].append(new_rank)



def players_sorted_by_final_rank():
    sorted_data = sorted(players.items(), key=lambda item: item[1]['rank'][-1])
    return sorted_data

def players_sorted_by_initial_rank():
    sorted_data = sorted(players.items(), key=lambda item: item[1]['rank'][0])
    return sorted_data

create_player('A1', random.randint(1500,2000), random.randint(10,20))
create_player('B1', random.randint(1500,2000), random.randint(10,20))
create_player('C1', random.randint(1500,2000), random.randint(10,20))
create_player('D1', random.randint(1500,2000), random.randint(10,20))

print('initial players info:')
print(players)
round_robin()
print('final players info:')
print(players)

print('all players sorted by final ranking: ')
print(players_sorted_by_final_rank())
print('all players, sorted by the change of their elo ranking from the start: ')
print(players_sorted_by_initial_rank())
