#!/usr/bin/python3
"""
Query the Reddit API for the titles of top ten posts of a given subreddit
"""
import requests


def top_ten(subreddit):
    """
        return top ten titles for a given subreddit
        return None if an invalid subreddit given
    """
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    req = requests.get(url, headers=headers).json()
    top_ten = req.get('data', {}).get('children', [])
    if not top_ten:
        print(None)
    for title in top_ten:
        print(title.get('data').get('title'))
