#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests
from sys import argv


def gather_data_from_an_API():
    """Gather data from an API"""
    # Get the user name
    url = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'
    response = requests.get(url)
    user = f'"{argv[1]}","{response.json().get("username")}"'
    # Get the todos for the user
    url = f'https://jsonplaceholder.typicode.com/todos?userId={argv[1]}'
    response = requests.get(url)
    todos = response.json()
    # Get the list of tasks and save them to a `.csv` file
    tasks = [task for task in todos]
    with open(f'{argv[1]}.csv', 'w') as file:
        for task in todos:
            task = f',"{task.get("completed")}","{task.get("title")}"\n'
            file.write(user + task)


if __name__ == "__main__":
    gather_data_from_an_API()
