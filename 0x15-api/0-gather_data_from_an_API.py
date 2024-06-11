#!/usr/bin/python3
"""a Python script """
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = f"https://jsonplaceholder.typicode.com"
    params = {'userId': employee_id}

    user = requests.get(f"{base_url}/users/{employee_id}").json()
    todos = requests.get(f"{base_url}/todos", params=params).json()

    completed = []
    for task in todos:
        if task.get("completed"):
            completed.append(task.get("title"))
    completed_count = len(completed)
    total_count = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    for task in completed:
        print("\t" + task)
