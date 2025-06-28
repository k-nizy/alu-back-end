#!/usr/bin/python3
"""
This script exports all tasks of a given employee to a JSON file using
the JSONPlaceholder REST API. The file is named as USER_ID.json.
"""

import json
import requests
import sys


def export_employee_tasks_to_json(employee_id):
    """Fetches all tasks of an employee and writes them to a JSON file."""
    base_url = "https://jsonplaceholder.typicode.com"

    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Employee not found.")
        sys.exit(1)
    user_data = user_response.json()
    username = user_data.get("username")

    todos_url = f"{base_url}/todos"
    todos_response = requests.get(todos_url, params={"userId": employee_id})
    todos = todos_response.json()

    task_list = []
    for task in todos:
        task_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    data = {str(employee_id): task_list}

    file_name = f"{employee_id}.json"
    with open(file_name, mode="w", encoding="utf-8") as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)
    export_employee_tasks_to_json(int(sys.argv[1]))
