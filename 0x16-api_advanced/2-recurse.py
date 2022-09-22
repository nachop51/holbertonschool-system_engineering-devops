#!/usr/bin/python3
"""Function that queries the Reddit API and returns a
list containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Returns a list of all posts of a subreddit """
    reddit_api = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }

    params = {
        'after': after,
        'limit': 100
    }

    response = requests.get(reddit_api, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    posts = response.json().get('data').get('children')

    posts = hot_list + [post.get('data').get('title') for post in posts]

    after = response.json().get('data').get('after')

    if after is not None:
        return recurse(subreddit, posts, after)
    return posts
