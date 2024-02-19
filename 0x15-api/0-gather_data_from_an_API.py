#!/usr/bin/python3
"""
Script to fetch and display an employee's TODO list progress from a REST API.

Usage: python script.py <employee_id>

Requirements:
- Uses the requests module for making HTTP requests.
- Accepts an integer as a parameter (employee ID).
- Displays the employee's TODO list progress in a specific format.

Example:
python script.py 4
"""
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
    employee_name = user_data.get('name')

    # Fetch user's TODO list
    todo_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    todo_data = todo_response.json()

    return employee_name, todo_data


def display_todo_progress(employee_name, todo_data):
    """
    Displays the employee's TODO list progress.

    Args:
        employee_name (str): The name of the employee.
        todo_data (list): The TODO list data.
    """
    total_tasks = len(todo_data)
    completed_tasks = [task for task in todo_data if task['completed']]
    num_completed_tasks = len(completed_tasks)

    print(
        f"Employee {employee_name} is done with tasks"
        f"({num_completed_tasks}/{total_tasks}):"
    )

    for task in completed_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    try:
        employee_name, todo_data = fetch_employee_data(employee_id)
        display_todo_progress(employee_name, todo_data)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
