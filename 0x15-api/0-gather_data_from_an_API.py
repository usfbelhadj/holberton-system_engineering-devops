#!/usr/bin/python3
'''Gather data from an API'''

import requests
import sys


if __name__ == "__main__":
    users_num = sys.argv[1]
    res = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                       .format(users_num))
    name = res.json().get('name')
    res1 = requests.get('https://jsonplaceholder.typicode.com/todos')
    dic = res1.json()
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
        jobs_id = res.json()
    print('Employee {} is done with tasks({}/{}):'.format(name, j, i))
    for s in list_title:
        print('\t {}'.format(s))
