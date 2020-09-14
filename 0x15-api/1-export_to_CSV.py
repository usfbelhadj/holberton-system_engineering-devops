#!/usr/bin/python3
'''Export to CSV'''

import requests
import sys


if __name__ == "__main__":

    users_num = sys.argv[1]

    res = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                       .format(users_num))
    username = res.json().get('username')
    res1 = requests.get('https://jsonplaceholder.typicode.com/todos')
    dic = res1.json()
    for d in dic:
        comp = d.get('completed')
        if d.get('userId') == int(users_num):
            f = open("{}.csv".format(users_num), "a")
            f.write('"{}","{}","{}","{}"'.
                    format(users_num, username, comp, d.get('title')))
            f.write("\n")
            f.close()
