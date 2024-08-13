#!/usr/bin/python3
"""
Using Reddit's API
"""
import requests

next_page = None


def recurse(subreddit, titles_list=[]):
    """Return top post titles recursively"""
    global next_page
    headers = {'User-Agent': 'custom-agent'}
    api_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': next_page}
    response = requests.get(api_url, params=params, headers=headers,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data")
        next_page = data.get("after")
        posts = data.get("children")

        for post in posts:
            titles_list.append(post.get("data").get("title"))

        if next_page is not None:
            fetch_hot_posts(subreddit, titles_list)

        return titles_list
    else:
        return None


# Example usage
if __name__ == "__main__":
    hot_posts = recurse("python")
    if hot_posts:
        for post in hot_posts[:10]:  # Displaying top 10 posts
            print(post)
