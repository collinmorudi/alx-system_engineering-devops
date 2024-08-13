#!/usr/bin/python3
"""Reddit API"""

import json
import requests


def count_words(subreddit, keywords, after_token="", word_counts=[]):
    """Count occurrences of keywords in subreddit titles"""

    if after_token == "":
        word_counts = [0] * len(keywords)

    api_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(api_url,
                            params={'after': after_token},
                            allow_redirects=False,
                            headers={'user-agent': 'custom-agent'})

    if response.status_code == 200:
        response_data = response.json()

        for post in response_data['data']['children']:
            title_words = post['data']['title'].split()
            for word in title_words:
                for index, keyword in enumerate(keywords):
                    if keyword.lower() == word.lower():
                        word_counts[index] += 1

        after_token = response_data['data']['after']
        if after_token is None:
            duplicates = []
            for i in range(len(keywords)):
                for j in range(i + 1, len(keywords)):
                    if keywords[i].lower() == keywords[j].lower():
                        duplicates.append(j)
                        word_counts[i] += word_counts[j]

            sorted_counts = sorted(zip(word_counts, keywords),
                                   key=lambda x: (-x[0], x[1].lower()))
            for count, keyword in sorted_counts:
                if count > 0 and keywords.index(keyword) not in duplicates:
                    print(f"{keyword.lower()}: {count}")
        else:
            count_words(subreddit, keywords, after_token, word_counts)


# Example usage
if __name__ == "__main__":
    count_words("python", ["Python", "requests", "API"])
