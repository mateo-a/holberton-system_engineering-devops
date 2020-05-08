#!/usr/bin/python3
"""recursive function that queries the Reddit API, parses the title of all
hot articles, and prints a sorted count of given keywords (case-insensitive,
delimited by spaces"""
import requests


def count_words(subreddit, word_list, after='', words={}):
    """count words"""
    if not word_list:
        return
    if not words:
        for w in words:
            words[w] = 0
    url = 'https://api.reddit.com/r/{}/hot?after={}'.format(subreddit, after)
    header = {'User-Agent': 'ubuntu:hbredditapp:v1.0.0 (by /u/mateo-a)'}
    response = requests.get(url, headers=header, allow_redirects=False,
                            params={'limit': 100})
    if response.status_code != 200:
        return None
    articles = response.json()['data']['children']
    for a in articles:
        title = a['data']['title'].lower().split()
        for t in title:
            if t in word_list:
                words.update
    after = response.json()['data']['after']
    if not after:
        if words:
            result = ["{}: {:d}".format(k, words[k]) for
                      k in sorted(words, key=words.get, reverse=True)]
            print("\n".join(result))
    else:
        return (count_words(subreddit, word_list, after, words))
