#!/usr/bin/python3
""" Script that fetches the endpoint https://jsonplaceholder.typicode.com/
    And process the data
"""
import sys
import requests


if __name__ == '__main__':
    id = int(sys.argv[1])
    res = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}').json()
    employee_name = res.get('username')
    filename = f"{id}.csv"
    res = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={id}').json()
    tasks_names = [task.get("title") for task in res]
    completed_status = [task.get("completed") for task in res]
    str = ""
    for status, task_name in zip(completed_status, tasks_names):
        str += f'"{id}","{employee_name}","{status}","{task_name}"\n'
    with open(filename, "w") as f:
        f.write(str)
