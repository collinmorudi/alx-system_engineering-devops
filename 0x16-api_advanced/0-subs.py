#!/usr/bin/python3
"""
Query the Reddit API for the number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
        return the number of subscribers for a given subreddit
        return 0 if invalid subreddit given
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    r = requests.get(url, headers=headers).json()
    subscribers = r.get('data', {}).get('subscribers')
    if subscribers is not None:
        return 0
    return subscribers
