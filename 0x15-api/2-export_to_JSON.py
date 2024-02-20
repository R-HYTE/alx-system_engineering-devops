#!/usr/bin/python3

"""
Python script that exports data in the JSON format.
"""

from requests import get
from sys import argv
import json


def fetch_user_data(user_id):
    """
    Fetches user data from the API based on the user ID.

    Args:
        user_id (int): The ID of the user.

    Returns:
        dict: User data if found, otherwise an empty dictionary.
    """
    user_response = get(
        f'https://jsonplaceholder.typicode.com/users/{user_id}'
    )
    return user_response.json()


def fetch_todo_list(user_id):
    """
    Fetches the TODO list for a specific user ID.

    Args:
        user_id (int): The ID of the user.

    Returns:
        list: List of TODO items for the user.
    """
    todo_response = get(
        f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
    )
    return todo_response.json()


def export_to_json(user_id, user_data, todo_list):
    """
    Exports TODO list data to a JSON file.

    Args:
        user_id (int): The ID of the user.
        user_data (dict): User data.
        todo_list (list): TODO list data.
    """
    filename = f'{user_id}.json'

    result = {str(user_id): []}

    for task in todo_list:
        result[str(user_id)].append({
            "task": task['title'],
            "completed": task['completed'],
            "username": user_data['username']
        })

    with open(filename, 'w') as file:
        json.dump(result, file)


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python script.py <user_id>")
        exit(1)

    user_id = int(argv[1])

    try:
        user_data = fetch_user_data(user_id)
        todo_list = fetch_todo_list(user_id)
        export_to_json(user_id, user_data, todo_list)

    except Exception as e:
        print(f"Error: {e}")
