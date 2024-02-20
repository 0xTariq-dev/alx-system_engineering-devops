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
    user = response.json().get('name')
    # Get the todos for the user
    url = f'https://jsonplaceholder.typicode.com/todos?userId={argv[1]}'
    response = requests.get(url)
    todos = response.json()
    # Get the list of completed tasks
    tasks = [task for task in todos if task.get('completed') is True]
    # Calculate the progress
    done, all = [len(tasks), len(todos)]
    # Print the progress and the tasks
    print(f"Employee {user} is done with tasks({done}/{all}):")
    [print("\t " + task.get('title')) for task in tasks]


if __name__ == "__main__":
    gather_data_from_an_API()
