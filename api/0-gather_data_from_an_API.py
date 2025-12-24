#!/usr/bin/python3

import requests
import sys


def get_employee_todo_progress(employee_id):
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"
    
    try:
        # Fetch user information
        user_response = requests.get(f"{base_url}/users/{employee_id}")
        user_response.raise_for_status()
        user_data = user_response.json()
        employee_name = user_data.get('name')
        
        # Fetch todos for the user
        todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
        todos_response.raise_for_status()
        todos = todos_response.json()
        
        # Calculate completed and total tasks
        completed_tasks = [todo for todo in todos if todo.get('completed')]
        total_tasks = len(todos)
        num_completed = len(completed_tasks)
        
        # Display the results
        print(f"Employee {employee_name} is done with tasks({num_completed}/{total_tasks}):")
        
        # Display completed task titles
        for task in completed_tasks:
            print(f"\t {task.get('title')}")
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}", file=sys.stderr)
        sys.exit(1)
    except (KeyError, ValueError) as e:
        print(f"Error parsing data: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>", file=sys.stderr)
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer", file=sys.stderr)
        sys.exit(1)
    
    get_employee_todo_progress(employee_id)
