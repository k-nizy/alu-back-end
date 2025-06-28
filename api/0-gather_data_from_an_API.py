#!/usr/bin/python3
"""Fetches and displays TODO list progress of a given employee

from the JSONPlaceholder REST API using their employee ID.
"""

import requests
import sys


def fetch_todo_progress(employee_id):
    """Fetch and display the TODO list progress for a given employee ID."""
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Fetch user info
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Error: Invalid employee ID")
        return
    user = user_response.json()
    employee_name = user.get("name")

    # Fetch TODO list
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Filter completed tasks
    done_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)
    num_done_tasks = len(done_tasks)

    # Display results
    print(f"Employee {employee_name} is doks({num_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            fetch_todo_progress(employee_id)
        except ValueError:
            print("Error: Employee ID must be an integer.")
