import json

files = ['org_chart_large','tech_company_org_chart_2','tech_company_org_chart_3']

all_data = []
for i in range(len(files)):
    f = open(f'{files[i]}.json')
    f_data = json.load(f)
    all_data.append(f_data)

def workers_num(num, data):
    # base condition
    if data['name']:
        num += 1
        # print(num, data['name'])
        if 'subordinates' in data.keys():
            for dict in data['subordinates']:
                num = workers_num(num, dict)
    return num

def workers_under_CTO(data):
    if data['name'] == 'CTO':
        res = workers_num(0, data)
        res -= 1
        return res
    elif 'subordinates' in data.keys():
        for i in data['subordinates']:
            return workers_under_CTO(i)

def developer_num(num, data):
    if data['name']:
        if 'Developer' in data['name']:
            num += 1
        if 'subordinates' in data.keys():
            for dict in data['subordinates']:
                num = developer_num(num, dict)
    return num

def departments(dep, data):
    if 'subordinates' in data.keys():
        dep.append(data['name'])
        for i in data['subordinates']:
            departments(dep, i)
    return len(dep), dep


for data in all_data:
    print('----------------------------')
    # how many workers? num of names
    print(workers_num(0,data))

    # how many workers under the CTO? num of names under CTO
    print(workers_under_CTO(data))

    # how many developers?
    print(developer_num(0, data))

    # how many departments ?
    print(departments([], data))