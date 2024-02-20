#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests
from sys import argv


def gather_data_from_an_API():
    """Gather data from an API"""
    user_id = argv[1]
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    response = requests.get(url)
    user = f'"{user_id}","{response.json().get("name")}"'
    url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
    response = requests.get(url)
    todos = response.json()
    tasks = [task for task in todos]
    with open(f'{user_id}.csv', 'w') as file:
        for task in todos:
            task = f',"{task.get("completed")}","{task.get("title")}"\n'
            file.write(user + task)


if __name__ == "__main__":
    gather_data_from_an_API()
