#● create variables describing 3 plants.
# ● for each plant - create 3 variables describing do they like sun
# or rain, how much water do they need, and do they like wind
# or not.
# ● ask for the user to describe the weather today - sun or clouds,
# precipitation number, and wind or not.
# ● for each condition - print what plant likes this condition.
# ● add a variable for each plant describing the amount of snow
# that will kill them.
# ● ask the user (in addition to the other conditions) for the snow
# info.
# ● print which plant is dead due to the snow


plants = [{'weather':'sun','water':15,'wind':True},{'weather':'sun','water':10,'wind':False},{'weather':'rain','water':5,'wind':True}]
weather_today = {'weather':'sun','water':15,'wind':True}

def who_like_the_weather(plants,weather_today):
    conditions = ['weather','water','wind']
    for i in conditions:
        for j in range(len(plants)):
            if plants[j][i] == weather_today[i]:
                print(f'plant {j} meet the {i} condition!')
            

who_like_the_weather(plants,weather_today)

snow_threshold = [3,4,9]
for i in range(len(plants)):
    plants[i]['snow'] = snow_threshold[i]


snow_today = 5
def check_who_dead(plants, snow_today):
    for i in range(len(plants)):
        if plants[i]['snow'] < snow_today:
            print(f'plant {i} will not survive!')

check_who_dead(plants, snow_today)