#!/usr/bin/python3

"""
Reddit API Top Ten Posts Module

This module provides a function to query the Reddit API
and print the titles of the first 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Retrieve and print the titles of the first 10 hot posts
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    user_agent = {
        'User-Agent': (
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 '
            'Safari/537.36'
        )
    }
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    response = requests.get(url, headers=user_agent)

    try:
        data = response.json()
        posts = data.get('data', {}).get('children', [])

        if not posts:
            print(None)
            return

        for post in posts:
            print(post['data']['title'])
    except (ValueError, KeyError):
        print(None)
