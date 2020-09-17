#!/usr/bin/python3
'''
Top Ten
'''
import json
import requests


def top_ten(subreddit):
    st = 'https://www.reddit.com/r/'+subreddit+'/hot.json'
    headers = {'User-agent': 'X11; Linux x86_64'}
    req = requests.get(st, headers=headers)
    data = req.json().get('data', None).get('children', None)
    if req.status_code != 200 or not data:
        print('None')
        return
    data = data[0:10]
    for t in data:
        print(t.get('data', {}).get('title', None))
