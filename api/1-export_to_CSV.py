#!/usr/bin/python3
"""Displays employee TODO list progress"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    EMPLOYEE_ID = sys.argv[1]
    API_URL = "https://jsonplaceholder.typicode.com"

    user = requests.get(f"{API_URL}/users/{EMPLOYEE_ID}").json()
    todos = requests.get(
        f"{API_URL}/todos",
        params={"userId": EMPLOYEE_ID}
    ).json()

    employee_name = user.get("name")
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task["completed"]]

    print(
        f"Employee {employee_name} is done with tasks"
        f"({len(done_tasks)}/{total_tasks}):"
    )

    for task in done_tasks:
        print(f"\t {task['title']}")
