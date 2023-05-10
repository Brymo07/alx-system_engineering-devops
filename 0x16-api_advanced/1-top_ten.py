#!/usr/bin/python3
"""
Module to request information from reditt API about any subreddit
"""
import requests


def top_ten(subreddit):
    """
    Method to request and get first 10 hot posts listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    headers = {
        'User-agent': "just me"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(None)
        return
    information = response.json()
    data = information["data"]
    children = data["children"]
    for i in range(0, 10):
        print(children[i]["data"]["title"])
