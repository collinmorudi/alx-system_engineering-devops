#!/usr/bin/python3
"""
Request from API to return TODO list progress of the given employee ID
"""

import requests
from sys import argv


def display():
    """return API data - Employee ID"""
    users = requests.get("http://jsonplaceholder.typicode.com/users")
    for u in users.json():
        if u.get('id') == int(argv[1]):
            NAME = (u.get('name'))
            break
    total = 0
    tasks = 0
    task_title = []
    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for t in todos.json():
        if t.get('userId') == int(argv[1]):
            total += 1
            if t.get('completed') is True:
                tasks += 1
                task_title.append(t.get('title'))
    print(f"Employee {NAME} is done with tasks({tasks}/{total}):")
    for task in task_title:
        print(f"\t {task}")


if __name__ == "__main__":
    display()
