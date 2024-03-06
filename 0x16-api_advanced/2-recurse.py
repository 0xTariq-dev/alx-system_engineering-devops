#!/usr/bin/python3
"""Module for returning the titles of all hot posts for a given subreddit"""

import requests
from sys import argv


def recurse(subreddit, hotlist=[], after=None):
    """Function that queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Chrome/56.0'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    hot_posts = response.json().get('data', {}).get('children', [])
    for post in hot_posts:
        hotlist.append(post.get('data', {}).get('title'))
    after = response.json().get('data', {}).get('after', None)
    if after:
        return recurse(subreddit, hotlist, after)
    return hotlist
