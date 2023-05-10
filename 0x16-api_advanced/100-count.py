#!/usr/bin/python3
""" raddit api"""

import requests

def count_words(subreddit, word_list, count=None, after=None):
    if count is None:
        count = {}
    if after is None:
        after = ''

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'myBot/0.0.1'}

    response = requests.get(url, headers=headers, params={'after': after}, allow_redirects=False)

    if response.status_code != 200:
        if after:
            count_words(subreddit, word_list, count, after=None)
        else:
            sorted_words = sorted(count.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_words:
                print(f"{word}: {count}")
        return

    data = response.json()['data']
    after = data['after']
    for child in data['children']:
        title = child['data']['title'].lower()
        for word in word_list:
            if word.lower() in title:
                if word in count:
                    count[word] += 1
                else:
                    count[word] = 1

    if after:
        count_words(subreddit, word_list, count, after)
    else:
        sorted_words = sorted(count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            print(f"{word}: {count}")
