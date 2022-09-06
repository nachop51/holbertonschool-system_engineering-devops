#!/usr/bin/python3
""" Script that fetches the endpoint https://jsonplaceholder.typicode.com/
    And process the data
"""
import json
import sys
import requests


if __name__ == '__main__':
    id = int(sys.argv[1])
    res = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}').json()
    employee_name = res.get('username')
    res = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={id}').json()
    new_json = {
        f"{id}": [{"task": task.get("title"),
                   "completed": task.get("completed"),
                   "username": employee_name} for task in res]
    }
    with open(f"{id}.json", "w") as f:
        json.dump(new_json, f)
