#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress."""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    if sys.argv[1]:
        id = int(sys.argv[1])
        name = requests.get("{}/users/{}"
                            .format(url, sys.argv[1])).json().get("name")
        if not name:
            exit()
        req = requests.get("{}/todos?userId={}".format(url, id)).json()
        taskCompleted = [t for t in req if t.get("completed") is True]
        print("Employee {} is done with tasks({}/{}):"
              .format(name, len(taskCompleted), len(req)))
        if taskCompleted:
            print("\t ", end="")
            print("\n\t ".join(t.get("title") for t in taskCompleted))
