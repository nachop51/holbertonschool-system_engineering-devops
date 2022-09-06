#!/usr/bin/python3
"""
    Script that fetches the endpoint https://jsonplaceholder.typicode.com/
    And process the data
"""
import json
import requests
import sys


if __name__ == '__main__':
    id = int(sys.argv[1])
    res = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(id)).json()
    employee_name = res.get('username')
    res = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(id)
    ).json()
    new_json = {
        "{}".format(id): [{"task": task.get("title"),
                           "completed": task.get("completed"),
                           "username": employee_name} for task in res]
    }
    with open("{}.json".format(id), "w") as f:
        json.dump(new_json, f)
