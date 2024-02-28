schedule = {}
def generate_schedule():
    for i in range(1,6):
        schedule[i]={key:"" for key in range(8,17)}

def handle_sys():
    generate_schedule()
    while True:
        print('add new task')
        print('when you finish adding tasks Enter:: no tasks in task name ')
        task_name = input('Enter task name: ')
        if task_name == 'no tasks':
            break
        duration = int(input('Enter task duration: '))
        day = int(input('Enter day from 1 to 5: '))
        time = int(input('Enter hour from 8 to 16: '))
        add_task(task_name, duration, day, time)
        print_schedule()


def add_task(task_name,duration,day = None, time = None):
    if day or time:
        if check_availability(duration, day, time) is True:
            print('choosen day and time not populated')
            # available
            populate_task(task_name, duration, day, time)
        else:
            # not available
            spoted_task , start, end = check_availability(duration,day, time)
            print(f'choosen time ARE populated with {spoted_task} from {start} to {end}')
            answer = input('do you want to choose new TIME? answer with yes or no')
            if answer == 'yes':
                day = int(input('choose day from 1 to 5: '))
                time = int(input('choose hour from 8 to 16: '))
                add_task(task_name, duration, day, time)
            if answer == 'no':
                # over write the new task
                populate_task(task_name, duration, day, time)
    else:
        day, time = find_spot(duration)
        populate_task(task_name,duration,day = None, time = None)

def populate_task(task_name,duration,day = None, time = None):
    for i in range(duration):
        schedule[day][time + i] = task_name
    print('task populated succesfully!')
def check_availability(duration, day = None, time = None):
    dur = 0
    for i in range(duration):
        if schedule[day][time+i] == '':
            dur += 1
    if dur == duration:# available
        return True
    else:
        spoted_task = schedule[day][time]
        spoted_time = []
        for i in range(8,17):
            if schedule[day][i] == spoted_task:
                spoted_time.append(i)
        return spoted_task, spoted_time[0], spoted_time[-1]

def find_spot(duration):
    spots = {}
    for day in range(1,6):
        available_hours = []
        for hour in range(8,17):
            if schedule[day][hour] == '':
                available_hours.append(hour)
        spots[day]= available_hours
    print(spots)
    # pick by duration
    spoted_by_dur = []
    for day, hours in spots.items():
        dur = 0
        for hour in hours:
            dur += 1
            if dur == duration:
                spoted_by_dur.append([day, hour-duration+1])
            if hour + 1 not in hours:
                dur = 0
    print(spoted_by_dur[0][0], spoted_by_dur[0][1])
    if spoted_by_dur:
        return spoted_by_dur[0][0], spoted_by_dur[0][1]
    else:
        print('no spots')

def print_schedule():
    print(schedule)

handle_sys()
