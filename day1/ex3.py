# We will simulate a dating app.
# ● create 4 users with different data.
# ● using the input function - create a user with the following
# attributes: name, gender, age, profession, favorite tv show,
# favorite food.
# ● create a set of rules for each attribute, which will give ok to the
# match (for example: age has to be between 20-30, food has to
# be pizza or salad, etc).
# ● check if the user given profile matches with any of the built in
# profiles.
# ● print the result.
# Extra:
# ● if the users don’t match - ask for the data again.


users = [{'name': 'A', 'gender': 'male', 'age': 25, 'profession': 'teacher', 'tvshow': 'friends','food': 'mexican'},
         {'name': 'B', 'gender': 'male', 'age': 45, 'profession': 'lawyer', 'tvshow': 'harry poter','food': 'italian'},
         {'name': 'C', 'gender': 'male', 'age': 20, 'profession': 'writer', 'tvshow': 'big bang','food': 'Chinese'},
         {'name': 'D', 'gender': 'male', 'age': 36, 'profession': 'doctor', 'tvshow': 'the 100','food': 'arabian'}]

def create_user():
    name, gender, age, profession, tvshow, food = input('Enter WITHOT SPASE!: name, gender, age, profession, tvshow, food ').split(',')
    new_user = {'name': name, 'gender': gender, 'age': age, 'profession': profession, 'tvshow': tvshow, 'food': food}
    return new_user


new_user = create_user()
# q,female,30,developer,friends,arabian
# a,male,2,a,a,a

def find_match(users, new_user):
    scores = [0 for i in range(len(users))]
    for i in range(len(users)):
        if new_user['gender'] != users[i]['gender']:
            scores[i] += 1
        if new_user['profession'] == users[i]['profession'] :
            scores[i] += 1
        if new_user['tvshow'] == users[i]['tvshow'] :
            scores[i] += 1
        if new_user['food'] == users[i]['food'] : 
            scores[i] += 1    
        if abs(int(new_user['age']) - int(users[i]['age'])) <= 10:
            scores[i] += 1
    for i in range(len(scores)):
        if scores[i] > 0:
            print(f'user {users[i]['name']} matches with score of {scores[i]}')
    if sum(scores) == 0:
        new_user = create_user()
        find_match(users, new_user)
        
find_match(users, new_user)
        
