#!/usr/bin/python3

"""
Reddit API Recursive Hot Articles Module

This module provides a recursive function to query the Reddit API and
return a list containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively retrieve the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles of hot articles.
        after (str): Parameter used for pagination in Reddit API.

    Returns:
        list or None: A list containing the titles of all hot articles.
            Returns None if no results are found or the subreddit is invalid.
    """
    if hot_list is None:
        hot_list = []

    if not subreddit or not isinstance(subreddit, str):
        return None

    user_agent = {
        'User-Agent': (
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 '
            'Safari/537.36'
        )
    }

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    if after:
        url += f'&after={after}'

    response = requests.get(url, headers=user_agent)

    try:
        data = response.json()
        posts = data.get('data', {}).get('children', [])

        if not posts:
            return hot_list

        for post in posts:
            hot_list.append(post['data']['title'])

        after = data.get('data', {}).get('after')
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list

    except (ValueError, KeyError):
        return None
