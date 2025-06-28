#!/usr/bin/python3
"""
This script exports all tasks of a given employee to a CSV file using
the JSONPlaceholder REST API. The file is named as USER_ID.csv.
"""

import csv
import requests
import sys


def export_employee_tasks_to_csv(employee_id):
    """Fetches all tasks of an employee and writes them to a CSV file."""
    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee info
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Employee not found.")
        sys.exit(1)
    user_data = user_response.json()
    username = user_data.get("username")

    # Get employee todos
    todos_url = f"{base_url}/todos"
    todos_response = requests.get(todos_url, params={"userId": employee_id})
    todos = todos_response.json()

    # Write to CSV file
    file_name = f"{employee_id}.csv"
    with open(file_name, mode="w", newline='', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                str(task.get("completed")),
                task.get("title")
            ])


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)
    export_employee_tasks_to_csv(int(sys.argv[1]))
