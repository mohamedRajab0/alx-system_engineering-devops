#!/usr/bin/python3
"""script for handle api"""
import requests


def number_of_subscribers(subreddit):
    """unction that queries the Reddit API and returns
    the number of subscribers
    for a given subreddit. If an invalid subreddit is given, the function
    should return 0."""

    base_url = f'https://www.reddit.com/r/{subreddit}/about.json'
    request = requests.get(base_url, headers={'User-agent': 'app/1.0'})
    if request.status_code == 200:
        data = request.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
