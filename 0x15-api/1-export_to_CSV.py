#!/usr/bin/python3
"""a Python script that, using
REST API, for a given employee ID,
returns information about his/her TODO list progress.
Python script to export data in the CSV format.
"""
import csv
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = f"https://jsonplaceholder.typicode.com"
    params = {'userId': employee_id}

    user = requests.get(f"{base_url}/users/{employee_id}").json()
    todos = requests.get(f"{base_url}/todos", params=params).json()

    with open(f"{employee_id}.csv", "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employee_id, user.get('username'),
                             task.get('completed'), task.get('title')])
