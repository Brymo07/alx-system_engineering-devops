#!/usr/bin/python3
""" raddit api"""

import json
import requests


def count_words(subreddit, word_list, after="", count=None, word_counts=None):
    if not word_counts:
        word_counts = {}

    if not count:
        count = [0] * len(word_list)

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'bhalut'}
    params = {'after': after}
    request = requests.get(url, params=params, headers=headers, allow_redirects=False)

    if request.status_code != 200:
        return

    data = request.json()

    for topic in data['data']['children']:
        for word in topic['data']['title'].split():
            word = word.lower().rstrip('.!_')
            if word in word_list:
                count[word_list.index(word)] += 1

    after = data['data']['after']

    if after is None:
        for i, word in enumerate(word_list):
            word_counts[word.lower()] = word_counts.get(word.lower(), 0) + count[i]

        word_counts = dict(sorted(word_counts.items(), key=lambda item: (-item[1], item[0])))

        for word, count in word_counts.items():
            if count > 0:
                print(f"{word}: {count}")
        return

    count_words(subreddit, word_list, after, count, word_counts)

