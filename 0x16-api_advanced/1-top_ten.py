#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """top ten posts"""
    url = 'https://api.reddit.com/r/{}/hot/'.format(subreddit)
    header = {'User-Agent': 'ubuntu:hbredditapp:v1.0.0 (by /u/mateo-a)'}
    response = requests.get(url, headers=header, allow_redirects=False,
                            params={'limit': 10})
    if response.status_code == 200:
        posts = response.json()['data']['children']
        for p in posts:
            print(p['data']['title']) 
    else:
        print('None')
