#!/usr/bin/python3

"""
Script to fetch and display an employee's TODO list progress from a REST API.
It also exports the data in JSON format.

Usage: python3 2-export_to_JSON.py <employee_id>
"""

import json
import requests
import sys


def fetch_employee_data(employee_id):
    """
    Fetches employee data including name and TODO list.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        tuple: A tuple containing the employee name and the TODO list data.
    """
    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch user data
    user_response = requests.get(f'{base_url}/users/{employee_id}')
    user_data = user_response.json()
    employee_username = user_data.get('username')

    # Fetch user's TODO list
    todo_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    todo_data = todo_response.json()

    return employee_username, todo_data


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        exit(1)

    employee_id = int(sys.argv[1])

    try:
        employee_username, todo_data = fetch_employee_data(employee_id)

        row = []

        for task in todo_data:
            new_dict = {
                "task": task["title"],
                "completed": task["completed"],
                "username": employee_username
            }
            row.append(new_dict)

        final_dict = {str(employee_id): row}
        json_obj = json.dumps(final_dict)

        with open(f'{employee_id}.json', 'w') as f:
            f.write(json_obj)

    except Exception as e:
        print(f"Error: {e}")
