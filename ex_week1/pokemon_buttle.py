player_1 = [{'name': 'A1', 'level': 1, 'strength': 3, 'speed': 2,'type': 'wind','life': 120},
            {'name': 'A2', 'level': 2, 'strength': 4, 'speed': 3,'type': 'water','life': 120},
            {'name': 'A3', 'level': 3, 'strength': 10, 'speed': 4,'type': 'earth','life': 120},
            {'name': 'A4', 'level': 4, 'strength': 8, 'speed': 5,'type': 'fire','life': 120},
            {'name': 'A5', 'level': 5, 'strength': 7, 'speed': 1,'type': 'water','life': 120}]

player_2 = [{'name': 'B1', 'level': 1, 'strength': 9, 'speed': 1,'type': 'earth','life': 120},
            {'name': 'B2', 'level': 2, 'strength': 8, 'speed': 2,'type': 'wind','life': 120},
            {'name': 'B3', 'level': 3, 'strength': 9, 'speed': 3,'type': 'fire','life': 120},
            {'name': 'B4', 'level': 4, 'strength': 6, 'speed': 4,'type': 'fire','life': 120},
            {'name': 'B5', 'level': 5, 'strength': 10, 'speed': 5,'type': 'water','life': 120}]

types = {'fire':{'stronger': ['earth'], 'weaker':['water','wind']},
         'water': {'stronger': ['wind'], 'weaker':['fire','earth']},
         'earth': {'stronger': ['water'], 'weaker':['fire','wind']},
         'wind': {'stronger': ['fire', 'earth'], 'weaker':['water']}}


import random
def select_pokemon_index(user):
    available_indices = [i for i in range(len(user)) if user[i]['life'] != 0]
    if available_indices:
        return random.choice(available_indices)

# output: 0 - user 1 attcks, 1 - user 2 attacks
def who_attack(pokemon_1, pokemon_2): 
    score = []
    random_score = random.randint(1, 20)
    score.append(random_score + pokemon_1['speed'])
    score.append(random_score + pokemon_2['speed'])  
    return score.index(max(score))

# output: 0 - pok1 stronger, 1 - pok2 stronger
def check_stronger(pokemon_1, pokemon_2):
    seq = types[pokemon_1['type']]
    # seq = [item for item in types if item["type"] == pokemon_1['type']][0]
    if pokemon_2['type'] in seq['weaker']:
        return 0
    else:
        return 1
    
def substract_damage(pokemon_1, pokemon_2, attacker, stronger):
    random_damage = random.randint(1,20)
    if attacker == stronger:
        if attacker == 1:
            pokemon_2 ['life'] = pokemon_2['life'] - 2*(random_damage-pokemon_2['strength'])
        if attacker == 0:
            pokemon_1 ['life'] = pokemon_1['life'] - 2*(random_damage-pokemon_1['strength'])
    elif attacker == 1 and stronger == 0:
        pokemon_2 ['life'] = pokemon_2['life'] - (random_damage-pokemon_2['strength'])
    elif attacker == 0 and stronger == 1:
        pokemon_1 ['life'] = pokemon_1['life'] - (random_damage-pokemon_1['strength'])

    if pokemon_1['life'] < 0:
        pokemon_1['life'] = 0 
    if pokemon_2['life'] < 0:
        pokemon_2['life'] = 0
    return pokemon_1,pokemon_2



def check_loser(pokemon_1, pokemon_2):
    # recursia base case
    if pokemon_1['life'] == 0 or pokemon_2['life'] == 0:
        return pokemon_1,pokemon_2
    
    stronger = check_stronger(pokemon_1, pokemon_2)
    attacker = who_attack(pokemon_1, pokemon_2)
    
    seq = types[pokemon_1['type']]
    # seq = [item for item in types if item["type"] == pokemon_1['type']][0]
    pok_2_in_weaker = pokemon_2['type'] in seq['weaker']
    # update life by substract_damage
    if pok_2_in_weaker:
        isStronger = pokemon_1
        isWeaker = pokemon_2
        pokemon_1,pokemon_2 = substract_damage(isStronger,isWeaker,attacker, stronger)
    else:
        isStronger = pokemon_2
        isWeaker = pokemon_1
        pokemon_2,pokemon_1 = substract_damage(isStronger,isWeaker,attacker, stronger)         
    return check_loser(pokemon_1, pokemon_2)


def select_fighters(user1, user2):
    # select fighters that have diffrent types
    indx1 = select_pokemon_index(user1)
    indx2 = select_pokemon_index(user2)
    print(indx1, indx2)
    if indx1 is None or indx2 is None:
        return None
    user1_pok = user1[indx1]
    user2_pok = user2[indx2]
    while user1_pok['type'] == user2_pok['type']:
        indx2 = select_pokemon_index(user2)
        if indx1 is None or indx2 is None:
            return None
        user2_pok = user2[indx2]
    return user1_pok, user2_pok


def fight(user1, used_poks1, user2, used_poks2):

    while used_poks1 < len(user1) + 1 and used_poks2 < len(user2) + 1:
        if select_fighters(user1, user2) is None:
            break
        else:
            user1_pok, user2_pok = select_fighters(user1, user2)
            print(f'zzzz:: {used_poks1}, {used_poks2}')
            
            user1_pok, user2_pok = check_loser(user1_pok, user2_pok)

                # one of the outputs is with life = 0, need to be replaced
                # print(user1_pok, user1_pok)
            if user1_pok['life'] <= 0:
                print('used_poks1 should +1')
                # print(user1_pok)
                used_poks1 += 1
                print(f'zzzz:: {used_poks1}, {used_poks2}')
                if used_poks1 >= len(user1) + 1:
                    break
                indx = select_pokemon_index(user1)
                if indx is None:
                    break
                else:
                    user1_pok = user1[indx]
            if user2_pok['life'] <= 0:
                print('used_poks2 should +1')
                # print(user2_pok)
                used_poks2 += 1 
                print(f'zzzz:: {used_poks1}, {used_poks2}')
                if used_poks2 >= len(user2)+1:
                    break
                indx = select_pokemon_index(user2)
                if indx is None:
                    break
                else:
                    user2_pok = user2[indx]

    if used_poks1 >= len(user1):
        print('the winner is user2')
    if used_poks2 >= len(user2):
        print('the winner is user1')
 

fight(player_1, 0, player_2, 0)




