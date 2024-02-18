# Task description:
# ● you are a boxing champion, and we will simulate
# your next fight.
# ● In boxing, there are common numbers for each
# basic move - see here.
# ● decide which boxing move beats other boxing
# moves. make sure that each boxing move wins at
# least against 1 move and losses to at least 1 move.
# ● lets simulate a boxing round - ask the user to select
# a number representing a boxing move. save it.
# ● randomly select a number in the range of 1-4, for
# your opponents move.
# ● compare your move and the opponent move - and
# according to the rules you set - decide who wins the
# round.
# ● print the round result.

moves = [{'move_num': 1,'stronger': [2],'weaker': [3,4,5,6]},
         {'move_num': 2,'stronger': [3,6],'weaker': [1,4,5]},
         {'move_num': 3,'stronger': [1,4],'weaker': [2,5,6]},
         {'move_num': 4,'stronger': [1,2,5],'weaker': [3,6]},
         {'move_num': 5,'stronger': [1,2,3,6],'weaker': [4]},
         {'move_num': 6,'stronger': [1,2,3,4],'weaker': [5]}]

import random
my_move = random.randint(1, 4)
print(f'my_move is {my_move}')

user_move = input('choose number between 1 - 6 : ')

def winner(user_move, my_move):
    if int(user_move) == int(my_move):
        print('same move!')
        user_move = input('choose number between 1 - 6 : ')
        winner(user_move, my_move)
    else:
        arr = [item for item in moves if item["move_num"] == int(user_move)][0]
        isStronger = int(my_move) in arr['weaker']
        if isStronger:
            print('user wins!')
        else:
            print('I win')

winner(user_move, my_move)
