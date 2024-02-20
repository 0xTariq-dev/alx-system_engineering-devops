#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests
from sys import argv


def gather_data_from_an_API():
    """Gather data from an API"""
    res = requests.get(f'https://jsonplaceholder.typicode.com/users/')
    users = res.json()
    users_list = {}
    for user in users:
        id, name = user.get("id"), user.get("username")
        res = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{user.get("id")}/todos'
            )
        todos = res.json()
        tasks = [{"username": name,
                  "task": task.get("title"),
                  "completed": task.get("completed")
                  } for task in todos]
        users_list[id] = tasks
    json_string = json.dumps(users_list, ensure_ascii=False)
    print(json_string)
    with open(f'todo_all_employees.json', 'w') as f:
        f.write(json_string)


if __name__ == "__main__":
    gather_data_from_an_API()
