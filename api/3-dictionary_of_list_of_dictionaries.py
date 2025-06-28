#!/usr/bin/python3
"""
This script exports all employees' TODO tasks using the JSONPlaceholder API.
Output is a JSON file: todo_all_employees.json
"""

import json
import requests


def export_all_tasks_to_json():
    """Fetches all users and todos, then writes them to a JSON file."""
    base_url = "https://jsonplaceholder.typicode.com"

    # Get all users
    users_response = requests.get(f"{base_url}/users")
    users = users_response.json()

    # Get all todos
    todos_response = requests.get(f"{base_url}/todos")
    todos = todos_response.json()

    # Map user_id to username
    user_map = {user["id"]: user["username"] for user in users}

    # Build final dictionary
    all_data = {}
    for todo in todos:
        user_id = todo["userId"]
        task_info = {
            "username": user_map[user_id],
            "task": todo["title"],
            "completed": todo["completed"]
        }
        if str(user_id) not in all_data:
            all_data[str(user_id)] = []
        all_data[str(user_id)].append(task_info)

    # Write to file
    with open("todo_all_employees.json", "w", encoding="utf-8") as f:
        json.dump(all_data, f)


if __name__ == "__main__":
    export_all_tasks_to_json()
