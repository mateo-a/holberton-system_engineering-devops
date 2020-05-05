#!/usr/bin/python3
"""Script to export data in the JSON format."""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    if sys.argv[1]:
        id = int(sys.argv[1])
        name = requests.get("{}/{}".format(url, id)).json().get("username")
        req = requests.get("{}/{}/todos".format(url, id)).json()
        with open("{}.json".format(id), mode="w", newline="") as f:
            json.dump({id: [{"task": t.get("title"),
                             "completed": t.get("completed"),
                             "username": name} for t in req]}, f)
