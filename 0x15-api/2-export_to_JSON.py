#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests
from sys import argv


def gather_data_from_an_API():
    """Gather data from an API"""
    # Get the user name
    res = requests.get(f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
    user = res.json().get("username")
    # Get the todos for the user
    res = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{argv[1]}/todos'
        )
    todos = res.json()
    # Get the list of tasks
    tasks = [{"task": task.get("title"),
              "completed": task.get("completed"),
              "username": user
              } for task in todos]
    # Create a dict of the user id and tasks, convert it to a JSON and print it
    user_tasks = {argv[1]: tasks}
    json_string = json.dumps(user_tasks, ensure_ascii=False)
    print(json_string)
    # Save the tasks to a `.json` file
    with open(f'{argv[1]}.json', 'w') as f:
        f.write(json_string)


if __name__ == "__main__":
    gather_data_from_an_API()
