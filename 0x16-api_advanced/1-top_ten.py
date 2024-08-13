#!/usr/bin/python3

"""
Prints the titles of the first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit
    """

    if not subreddit or not isinstance(subreddit, str):
        print("None")
        return

    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 10}
    api_url = f'https://www.reddit.com/r/{subreddit}/hot/.json'

    response = requests.get(api_url, headers=headers, params=params)
    if response.status_code != 200:
        print("None")
        return

    try:
        data = response.json().get('data', {}).get('children', [])
        for post in data:
            print(post.get('data', {}).get('title', 'No Title'))
    except Exception:
        print("None")


# Example usage
if __name__ == "__main__":
    top_ten("python")
