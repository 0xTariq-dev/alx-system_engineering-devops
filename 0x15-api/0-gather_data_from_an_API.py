#!/usr/bin/python3
"""Gather data from an API"""
import requests
from sys import argv
import json


def gather_data_from_an_API():
    """Gather data from an API"""
    user_id = argv[1]
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    response = requests.get(url)
    user = response.json().get('name')
    url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
    response = requests.get(url)
    todos = response.json()
    tasks = [task for task in todos if task.get('completed') is True]
    prog = [len(tasks), len(todos)]
    print(f"Employee {user} is done with tasks({prog[1]}/{prog[2]}):")
    [print("\t " + task.get('title')) for task in tasks]


if __name__ == "__main__":
    gather_data_from_an_API()
