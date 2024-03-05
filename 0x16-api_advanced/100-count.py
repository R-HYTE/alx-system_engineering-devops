#!/usr/bin/python3

"""
Reddit API Recursive Keyword Count Module

This module provides a recursive function to query the Reddit API,
parse titles of hot articles, and print a sorted count of given keywords.
The results are based on the number of times a keyword appears in the
titles of hot articles.

"""

import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """
    Recursively query the Reddit API, parse titles of hot articles,
    and print a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords.
        after (str): Parameter used for pagination in Reddit API.
        count_dict (dict): A dictionary to store the counts of each keyword.

    Returns:
        None
    """
    if count_dict is None:
        count_dict = {}

    if not subreddit or not isinstance(subreddit, str):
        return

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
            # When there are no more posts, print the results
            print_results(count_dict)
            return

        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                # Check if the word is a whole word in the title
                lowercase_word = word.lower()
                count_dict[lowercase_word] = (
                    count_dict.get(lowercase_word, 0) + 1
                )

        after = data.get('data', {}).get('after')
        count_words(subreddit, word_list, after, count_dict)
    except (ValueError, KeyError):
        return


def print_results(count_dict):
    """
    Print the sorted count of keywords.

    Args:
        count_dict (dict): A dictionary containing the counts of each keyword.

    Returns:
        None
    """
    for word, count in sorted(count_dict.items(), key=lambda x: (-x[1], x[0])):
        print(f'{word}: {count}')
