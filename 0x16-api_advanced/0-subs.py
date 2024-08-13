#!/usr/bin/python3
"""
Retrieve the number of subscribers for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """

    if not subreddit or not isinstance(subreddit, str):
        return 0

    headers = {'User-Agent': 'Mozilla/5.0'}
    api_url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(api_url, headers=headers)

    if response.status_code != 200:
        return 0

    try:
        data = response.json().get('data', {})
        return data.get('subscribers', 0)
    except Exception:
        return 0


# Example usage
if __name__ == "__main__":
    subreddit_name = "python"
    subscribers = number_of__subscribers(subreddit_name)
    print(f"Number of subscribers in r/{subreddit_name}: {subscribers}")
