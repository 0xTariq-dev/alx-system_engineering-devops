#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests
from sys import argv


def gather_data_from_an_API():
    """Gather todos progress for all employees from an API"""
    # Get the users list
    res = requests.get(f'https://jsonplaceholder.typicode.com/users/')
    users = res.json()
    users_list = {}
    # Get the todos for each user and store them in a dictionary
    for user in users:
        # Get the user id and name from the users dictionary
        id, name = user.get("id"), user.get("username")
        # Get the todos for each user
        res = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{id}/todos'
            )
        todos = res.json()
        # Store the todos in a dictionary with the user id as the key.
        tasks = [{"username": name,
                  "task": task.get("title"),
                  "completed": task.get("completed")
                  } for task in todos]
        users_list[id] = tasks
    # Format the data, Print the data to the stdout and save it to a file.
    json_string = json.dumps(users_list, ensure_ascii=False)
    print(json_string)
    with open(f'todo_all_employees.json', 'w') as f:
        f.write(json_string)


if __name__ == "__main__":
    gather_data_from_an_API()
