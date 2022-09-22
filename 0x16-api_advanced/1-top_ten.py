#!/usr/bin/python3
"""
    Function that queries the Reddit API and prints
    the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """ Prints the top ten hot posts of a subreddit """
    reddit_api = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }

    params = {
        'limit': 10
    }

    response = requests.get(reddit_api, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json().get('data').get('children')
        for post in posts:
            print(post.get('data').get('title'))
    else:
        print("None")
