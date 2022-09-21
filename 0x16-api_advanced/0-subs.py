#!/usr/bin/python3
"""
    Function that queries the Reddit API
    and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """ Return the number of subscribers of a subreddit """
    reddit_api = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }

    response = requests.get(reddit_api, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    return 0
