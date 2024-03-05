#!/usr/bin/python3
"""
Reddit API Subscribers Module

This module provides a function to query the Reddit API and retrieve
the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Retrieve the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit.
        Returns 0 if the subreddit is invalid.
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-Agent': 'My-User-Agent/1.0 (by /u/your_username)'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=user_agent)
    all_data = response.json()

    try:
        return all_data.get('data').get('subscribers')
    except:
        return 0
