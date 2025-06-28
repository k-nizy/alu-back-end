#!/usr/bin/python3
"""
This script retrieves and displays the TODO list progress of a given employee
using the JSONPlaceholder REST API.

Usage:
    ./0-gather_data_from_an_API.py <employee_id>
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """Fetches and prints the TODO progress for a given employee."""
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee details
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Employee not found.")
        sys.exit(1)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch employee todos
    todos_url = f"{base_url}/todos"
    todos_response = requests.get(todos_url, params={"userId": employee_id})
    todos = todos_response.json()

    # Filter completed tasks
    done_tasks = [task for task in todos if task.get("completed") is True]
    total_tasks = len(todos)
    done_count = len(done_tasks)

    # Print progress
    print(
        f"Employee {employee_name} is done with tasks({done_count}/{total_tasks}):"
    )
    for task in done_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    get_employee_todo_progress(int(sys.argv[1]))

