#!/usr/bin/python3
"""
Script to fetch and display an employee's TODO list progress from a REST API.
It also exports the data in JSON format.

Usage: python script.py <employee_id>

Requirements:
- Uses the requests module for making HTTP requests.
- Accepts an integer as a parameter (employee ID).
- Displays the employee's TODO list progress in a specific format.
- Exports TODO list data in JSON format to a file named USER_ID.json.

Example:
python3 2-export_to_JSON.py 2
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


def export_to_json(employee_id, employee_username, todo_data):
    """
    Exports TODO list data in JSON format to a file named USER_ID.json.

    Args:
        employee_id (int): The ID of the employee.
        employee_username (str): The username of the employee.
        todo_data (list): The TODO list data.
    """
    output_data = {
            str(employee_id): [
                {
                    "task": task['title'],
                    "completed": task['completed'],
                    "username": employee_username
                }
                for task in todo_data
            ]
    }

    with open(f'{employee_id}.json', 'w') as json_file:
        json.dump(output_data, json_file, indent=2)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    try:
        employee_username, todo_data = fetch_employee_data(employee_id)
        export_to_json(employee_id, employee_username, todo_data)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
