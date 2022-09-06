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
    employee_name = res.get('name')
    res = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={id}').json()
    total_tasks = len(res)
    completed_tasks = len([task for task in res if task.get('completed')])
    pending_tasks = "\t " + "\t ".join([str(task.get('title') + "\n")
                                        for task in res if task.get('completed')])
    print(f"Employee {employee_name} is \
done with tasks({completed_tasks}/{total_tasks}):\n{pending_tasks}", end="")
