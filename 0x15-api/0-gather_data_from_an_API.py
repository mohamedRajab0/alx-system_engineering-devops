#!/usr/bin/python3
"""a Python script that, using
REST API, for a given employee ID,
returns information about his/her TODO list progress.
script  display on the standard output the employee TODO list progress.
First line:
Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/
TOTAL_NUMBER_OF_TASKS):

EMPLOYEE_NAME: name of the employee
NUMBER_OF_DONE_TASKS: number of completed tasks
TOTAL_NUMBER_OF_TASKS: total number of tasks,
which is the sum of completed and non-completed tasks
Second and N next lines display the title of completed tasks:
TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
"""
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
