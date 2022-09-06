#!/usr/bin/python3
"""
    Script that fetches the endpoint https://jsonplaceholder.typicode.com/
    And process the data
"""
import json
import requests
import sys


if __name__ == '__main__':
    response = requests.get(
        'https://jsonplaceholder.typicode.com/users/').json()
    names = [name.get("username") for name in response]
    res = requests.get(
        'https://jsonplaceholder.typicode.com/todos').json()
    new_json = {
        r.get("id"): [{"username": names[int(task.get("userId")) - 1],
                       "task": task.get("title"),
                       "completed": task.get("completed")}
                      for task in res if task.get("userId") == r.get("id")]
        for r in response
    }
    with open("todo_all_employees.json", "w") as f:
        json.dump(new_json, f)
