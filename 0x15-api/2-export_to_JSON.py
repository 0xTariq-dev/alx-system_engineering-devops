#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests
from sys import argv


def gather_data_from_an_API():
    """Gather data from an API"""
    res = requests.get(f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
    user = res.json().get("username")
    res = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{argv[1]}/todos'
        )
    todos = res.json()
    tasks = [{"task": task.get("title"),
              "completed": task.get("completed"),
              "username": user
              } for task in todos]

    user_tasks = {argv[1]: tasks}
    json_string = json.dumps(user_tasks, ensure_ascii=False)
    print(json_string)


if __name__ == "__main__":
    gather_data_from_an_API()
