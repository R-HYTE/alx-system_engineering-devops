#!/usr/bin/python3

"""
Python script to export data in the CSV format.
"""

from requests import get
from sys import argv
import csv


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


def export_to_csv(employee_id, employee_name, todo_data):
    """
    Exports TODO list data to a CSV file.

    Args:
        employee_id (int): The ID of the employee.
        employee_name (str): The name of the employee.
        todo_data (list): TODO list data.
    """
    csv_filename = f'{employee_id}.csv'

    with open(csv_filename, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        
        # Write the first line with values
        writer.writerow([employee_id, employee_name, todo_data[0]['completed'], todo_data[0]['title']])

        for task in todo_data[1:]:
            writer.writerow([employee_id, employee_name, task['completed'], task['title']])


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python script.py <employee_id>")
        exit(1)

    employee_id = int(argv[1])

    try:
        employee_name, todo_data = fetch_employee_data(employee_id)
        export_to_csv(employee_id, employee_name, todo_data)

        print(f'Data exported to {employee_id}.csv')
    except Exception as e:
        print(f"Error: {e}")
