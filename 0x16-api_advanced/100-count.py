#!/usr/bin/python3
""" raddit api"""

import requests


def count_words(subreddit, word_list, after=None, word_count=None):
    """
    Recursively query the Reddit API and count the occurrences of given words in the titles of hot articles.
    Print a sorted count of the words in descending order, by the count, and if the count is the same for separate
    keywords, they should then be sorted alphabetically (ascending, from A to Z).
    """
    if word_count is None:
        word_count = {}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-agent': "just me"
    }
    params = {
        'limit': 100,
        'after': after
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return

    data = response.json()['data']
    for post in data['children']:
        title = post['data']['title'].lower()
        for word in word_list:
            if (word not in word_count) and (word.lower() in title):
                word_count[word] = 1
            elif (word in word_count) and (word.lower() in title):
                word_count[word] += 1

    if data['after'] is not None:
        return count_words(subreddit, word_list, data['after'], word_count)

    sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_word_count:
        print("{}: {}".format(word.lower(), count))

