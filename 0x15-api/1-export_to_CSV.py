#!/usr/bin/python3

"""
Python script that exports TODO list data in CSV format for a specific user ID.
"""

import csv
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


def export_to_csv(user_id, user_data, todo_data):
    """
    Exports TODO list data to a CSV file.

    Args:
        user_id (int): The ID of the user.
        user_data (dict): User data.
        todo_data (list): TODO list data.
    """
    filename = f'{user_id}.csv'

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for todo in todo_data:
            row = [
                str(todo['userId']),
                user_data['username'],
                'True' if todo['completed'] else 'False',
                todo['title']
            ]
            writer.writerow(row)


def main():
    if len(argv) != 2:
        print("Usage: python script.py <user_id>")
        exit(1)

    user_id = int(argv[1])

    try:
        todo_data = fetch_todo_data(user_id)
        user_data = fetch_user_data(user_id)
        export_to_csv(user_id, user_data, todo_data)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
