#!/usr/bin/python3
"""Module for Searching given keywords in a subreddit's hot titles"""

import requests
from sys import argv


def count_words(subreddit, word_list, after=""):
    """Prints the count of the given words in the subreddit's hot titles"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Chrome/56.0'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    hot_posts = response.json().get('data', {}).get('children', [])
    word_count = {}
    for post in hot_posts:
        title = post.get('data', {}).get('title')
        # print(title)
        for word in word_list:
            if word in title:
                if word in word_count:
                    word_count[word] += title.count(word)
                else:
                    word_count[word] = title.count(word)
    after = response.json().get('data', {}).get('after', None)
    if after:
        return count_words(subreddit, word_list, after)
    else:
        sorted_words = sorted(word_count.items(), key=lambda x: x[1],
                              reverse=True)
        for word, count in sorted_words:
            print('{}: {}'.format(word, count) if count > 0 else '', end='\n')
    return None
