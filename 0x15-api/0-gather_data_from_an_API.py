#!/usr/bin/python3
'''Gather data from an API'''
import requests
import json
import sys

if __name__ == "__main__":

    users_num = sys.argv[1]

    res = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                       .format(users_num ))
    name = json.loads(res.text).get('name')
    res1 = requests.get('https://jsonplaceholder.typicode.com/todos')
    dic = json.loads(res1.text)
    i = 0
    j = 0
    list_title = []
    for d in dic:
        if d.get('userId') == int(users_num):
            i += 1
            for k, v in d.items():
                if k == 'completed' and str(v) == 'True':
                    j += 1
                    list_title.append(d.get('title'))
    if dic == sys.argv[1]:
        jobs_id = json.loads(res.text)
        print(jobs_id)
    print(list_title)
    print('Employee {} is done with tasks({}/{}):'.format(name, j, i))
    for s in list_title:
        print('\t {}'.format(s))
