#!/usr/bin/python3
"""Script to use a REST API for a given employee ID, returns
information about his/her TODO list progress"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_id = sys.argv[1]
    api_url = "https://jsonplaceholder.typicode.com"

    # Get employee info
    user = requests.get(f"{api_url}/users/{employee_id}").json()
    if "name" not in user:
        sys.exit(1)

    # Get employee todos
    todos = requests.get(
        f"{api_url}/todos",
        params={"userId": employee_id}
    ).json()

    done_tasks = [task for task in todos if task.get("completed")]

    print(
        f"Employee {user['name']} is done with tasks ({len(done_tasks)}/{len(todos)}):")

    for task in done_tasks:
        print(f"\t {task['title']}")
