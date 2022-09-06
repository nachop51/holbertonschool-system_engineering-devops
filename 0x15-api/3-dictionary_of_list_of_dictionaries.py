#!/usr/bin/python3
""" Script that fetches the endpoint https://jsonplaceholder.typicode.com/
    And process the data
"""
import json
import sys
import requests


if __name__ == '__main__':
    response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/').json()
    names = [name.get("name") for name in response]
    filename = f"todo_all_employees.json"
    res = requests.get(
        f'https://jsonplaceholder.typicode.com/todos').json()
    new_json = {
        r.get("id"): [{"username": names[int(task.get("userId")) - 1],
                       "task": task.get("title"),
                       "completed": task.get("completed")}
                      for task in res if task.get("userId") == r.get("id")]
        for r in response
    }
    with open(filename, "w") as f:
        json.dump(new_json, f)
