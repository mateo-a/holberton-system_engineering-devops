#!/usr/bin/python3
"""recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit. If no
results are found for the given subreddit, the function should return None"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """top ten posts"""
    url = 'https://api.reddit.com/r/{}/hot?after={}'.format(subreddit, after)
    header = {'User-Agent': 'ubuntu:hbredditapp:v1.0.0 (by /u/mateo-a)'}
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code != 200:
        return None
    articles = response.json()['data']['children']
    for a in articles:
        hot_list.append(a)
    after = response.json()['data']['after']
    if not after:
        return hot_list
    else:
        return (recurse(subreddit, hot_list, after))
