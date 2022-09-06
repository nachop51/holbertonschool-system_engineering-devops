#!/usr/bin/python3
"""
    Script that fetches the endpoint https://jsonplaceholder.typicode.com/
    And process the data
"""
import requests
import sys


if __name__ == '__main__':
    id = int(sys.argv[1])

    res = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(id)).json()
    employee_name = res.get('name')
    res = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(id)
    ).json()
    total_tasks = len(res)
    completed_tasks = len([task for task in res if task.get('completed')])
    pending_tasks = "\t " + "\t ".join(
        [str(task.get('title') + "\n")
         for task in res if task.get('completed')]
    )
    print("Employee {} is \
done with tasks({}/{}):\n{}".format(
        employee_name, completed_tasks, total_tasks, pending_tasks), end="")
