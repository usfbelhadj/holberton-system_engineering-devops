#!/usr/bin/python3
'''Export to JSON'''
import requests
import json
import sys


if __name__ == "__main__":
    users_num = sys.argv[1]
    list_task = []
    di = {}
    d1 = {}
    res = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                       .format(users_num))
    username = res.json().get('username')
    res1 = requests.get('https://jsonplaceholder.typicode.com/todos')
    dic = res1.json()
    for d in dic:
        comp = d.get("completed")
        if d.get("userId") == int(users_num):
            di = {"task": d.get("title"),
                  "completed": comp, "username": username}
            list_task.append(di)
    d1 = {users_num: list_task}
    f = open("{}.json".format(users_num), "w+")
    f.write(str(json.dumps(d1)))
    f.close()
