#!/usr/bin/python3

"""
Python script that exports data in the JSON format.
"""

from requests import get
from sys import argv
import json


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
    user_response = get(f'{base_url}/users/{employee_id}')
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch user's TODO list
    todo_response = get(f'{base_url}/todos?userId={employee_id}')
    todo_data = todo_response.json()

    return employee_name, todo_data


def export_to_json(employee_id, employee_name, todo_data):
    """
    Exports TODO list data to a JSON file.

    Args:
        employee_id (int): The ID of the employee.
        employee_name (str): The name of the employee.
        todo_data (list): TODO list data.
    """
    json_filename = f'{employee_id}.json'

    row = []

    for task in todo_data:
        new_dict = {
            'username': employee_name,
            'task': task['title'],
            'completed': task['completed']
        }
        row.append(new_dict)

    final_dict = {employee_id: row}
    json_obj = json.dumps(final_dict)

    with open(json_filename, 'w') as json_file:
        json_file.write(json_obj)


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python script.py <employee_id>")
        exit(1)

    employee_id = int(argv[1])

    try:
        employee_name, todo_data = fetch_employee_data(employee_id)
        export_to_json(employee_id, employee_name, todo_data)

        print(f'Data exported to {employee_id}.json')
    except Exception as e:
        print(f"Error: {e}")
