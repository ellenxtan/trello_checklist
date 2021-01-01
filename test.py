import json
import os

def gen_res(f):
    with open(f) as json_file: 
        json_d = json.load(json_file) 

    checklist = json_d['checklists']

    c_lst = checklist[0]['checkItems']
    a_lst = checklist[1]['checkItems']

    states = []
    names = []
    for i in c_lst:
        states.append(i['state'])
        names.append(i['name'])
    for i in a_lst:
        states.append(i['state'])
        names.append(i['name'])

    return(states, names)


path = 'week/'

files = os.listdir(path)

res_d = dict()
for f in files:
    print(f)
    states, names = gen_res(path+f)
    assert len(states)==len(names)
    for i, name in enumerate(names):
        if name not in res_d:
            res_d[name] = 0
        if states[i] == 'complete':
            res_d[name] += 1

print(res_d)

import csv
with open('res.csv', 'w') as f:
    for key in res_d.keys():
        f.write("%s,%s\n"%(key,res_d[key]))