#!/usr/bin/python3
"""
Module to request information from reditt API about any subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Method to request and get the numbers of suscribers of a subreddit
    """
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    headers = {
        'User-agent': "just me"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return 0
    information = response.json()
    data = information["data"]
    subscribers = data["subscribers"]
    return (subscribers)
