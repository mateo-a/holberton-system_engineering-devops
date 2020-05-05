#!/usr/bin/python3
"""script to export data in the JSON format."""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    allUsers = requests.get(url).json()
    with open("todo_all_employees.json", mode="w", newline="") as f:
        json.dump({u.get("id"): [{"task": t.get("title"), "completed":
                                 t.get("completed"), "username":
                                 u.get("username")} for t in
                                 requests.get("{}/{}/todos"
                                 .format(url, u.get("id")))
                                 .json()] for u in allUsers}, f)
