materials = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T']
aligns = []

import random
for i in range(4):
    a = []
    option1, option2, option3 = random.sample(range(0, 20), 3)
    a.append(materials[option1])
    a.append(materials[option2])
    a.append(materials[option3])
    aligns.append({'name': i, 'needed_materials': a,'num_sug':random.randint(1,5)})

print(aligns)

def new_material(num_try):
    my_material = input('Enter material - capital letter from A - T:')
    num_try += 1
    return num_try, my_material

def negotiation():
    num_try, my_material = new_material(0)
    agree = []
    for i in range(len(aligns)):
        print(F'NEGOTION WITH : {aligns[i]['name']}')
        while my_material not in aligns[i]['needed_materials']:
            if num_try < aligns[i]['num_sug']:
                num_try, my_material = new_material(num_try)
            else: 
                agree.append(0)
                break
        else:
             agree.append(1)
             continue
        
    if sum(agree) >= 0.7:
        print(f'YOU SUCCEEDED WITH {sum(agree)/len(agree)}%')
    else:
        print(f'YOU FAILED WITH {sum(agree)/len(agree)}%')


negotiation()


