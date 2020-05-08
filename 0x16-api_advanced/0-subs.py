#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0"""
import requests


def number_of_subscribers(subreddit):
    """number of subscribers"""
    url = 'https://api.reddit.com/r/{}/about/'.format(subreddit)
    header = {'User-Agent': 'ubuntu:hbredditapp:v1.0.0 (by /u/mateo-a)'}
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 200:
        subscribers = response.json()['data']['subscribers']
    else:
        return 0
    return subscribers
