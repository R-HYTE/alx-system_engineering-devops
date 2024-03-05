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

    user_agent = {'User-Agent': 'Chrome/122.0.0.0'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=user_agent)

    try:
        all_data = response.json()
        # Check if 'data' key is present before accessing 'subscribers'
        if 'data' in all_data:
            return all_data['data'].get('subscribers', 0)
        else:
            return 0
    except (ValueError, KeyError):
        return 0
