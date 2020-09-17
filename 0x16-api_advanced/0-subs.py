#!/usr/bin/python3
'''
How many subs
'''
import requests


def number_of_subscribers(subreddit):
    st = 'https://www.reddit.com/r/'+subreddit+'/about.json'
    headers = {'User-agent': 'X11; Linux x86_64'}

    req = requests.get(st, headers=headers)
    if req.status_code != 200:
        return 0
    return(req.json().get('data', {}).get('subscribers', 0))
