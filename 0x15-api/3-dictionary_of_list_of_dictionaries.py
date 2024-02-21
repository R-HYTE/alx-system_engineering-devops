#!/usr/bin/python3

"""
Script to fetch and display TODO list progress -
from a REST API for all employees.
It also exports the data in JSON format.

Usage: python3 3-dictionary_of_list_of_dictionaries.py
"""

import json
import requests


def fetch_all_employee_data():
    """
    Fetches TODO list data for all employees.

    Returns:
        dict: A dictionary containing TODO list data for all employees.
    """
    base_url = 'https://jsonplaceholder.typicode.com/users'
    all_employee_data = {}

    try:
        # Fetch all users
        users_response = requests.get(base_url)
        users_data = users_response.json()

        for user in users_data:
            user_id = user['id']
            username = user['username']

            # Fetch user's TODO list
            todo_response = requests.get(
                f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
            )
            todo_data = todo_response.json()

            # Format tasks for the user
            tasks = [
                {
                    "username": username,
                    "task": task["title"],
                    "completed": task["completed"]
                }
                for task in todo_data
            ]

            all_employee_data[str(user_id)] = tasks

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

    return all_employee_data


if __name__ == "__main__":
    try:
        all_employee_data = fetch_all_employee_data()

        with open('todo_all_employees.json', 'w') as f:
            json.dump(all_employee_data, f, separators=(', ', ': '))

    except Exception as e:
        print(f"Error: {e}")
