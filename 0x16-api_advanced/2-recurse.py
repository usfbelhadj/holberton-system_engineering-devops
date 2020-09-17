#!/usr/bin/python3
'''
Recurse it
'''


import requests


def recurse(subreddit, hot_list=[], after=''):
    '''recurse'''
    st = 'https://www.reddit.com/r/'+subreddit+'/hot.json?after='+after
    headers = {'User-agent': 'X11; Linux x86_64'}
    req = requests.get(st, headers=headers)
    if req.status_code != 200:
        return None
    data = req.json().get('data', {}).get('children', {})
    for i in data:
        hot_list.append(i.get('data').get('title'))
    after = req.json().get('data', {}).get('after')
    if not after:
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
