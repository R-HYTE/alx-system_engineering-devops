#!/usr/bin/python3

"""
Python script to export TODO list data in JSON format for a specific user ID.
"""

import json
import requests
from sys import argv


def fetch_todo_data(user_id):
    """
    Fetch TODO list data for a specific user ID.

    Args:
        user_id (int): The ID of the user.

    Returns:
        list: List of TODO items for the user.
    """
    url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
    response = requests.get(url)
    return response.json()


def fetch_user_data(user_id):
    """
    Fetch user data based on user ID.

    Args:
        user_id (int): The ID of the user.

    Returns:
        dict: User data if found, otherwise an empty dictionary.
    """
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    response = requests.get(url)
    return response.json()


def export_to_json(user_id, user_data, todo_data):
    """
    Exports TODO list data to a JSON file.

    Args:
        user_id (int): The ID of the user.
        user_data (dict): User data.
        todo_data (list): TODO list data.
    """
    data_to_export = {str(user_id): []}

    for todo in todo_data:
        task_info = {
            "task": todo["title"],
            "completed": todo["completed"],
            "username": user_data["username"]
        }
        data_to_export[str(user_id)].append(task_info)

    filename = f'{user_id}.json'

    with open(filename, 'w') as file:
        json.dump(data_to_export, file)


def main():
    if len(argv) != 2:
        print("Usage: python script.py <user_id>")
        exit(1)

    user_id = int(argv[1])

    try:
        todo_data = fetch_todo_data(user_id)
        user_data = fetch_user_data(user_id)
        export_to_json(user_id, user_data, todo_data)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
