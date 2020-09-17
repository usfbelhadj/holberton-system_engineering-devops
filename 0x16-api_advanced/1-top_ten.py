#!/usr/bin/python3
'''
Top Ten
'''


import requests


def top_ten(subreddit):
    '''top_ten'''
    st = 'https://www.reddit.com/r/'+subreddit+'/hot.json'
    headers = {'User-agent': 'X11; Linux x86_64'}
    req = requests.get(st, headers=headers)
    if req.status_code != 200:
        print(None)
        return
    data = req.json().get('data', {}).get('children', {})
    data = data[0:10]
    for t in data:
        print(t.get('data', {}).get('title'))
