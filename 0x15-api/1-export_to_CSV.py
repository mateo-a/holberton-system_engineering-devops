#!/usr/bin/python3
"""script to export data in the CSV format."""
import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    if sys.argv[1]:
        id = int(sys.argv[1])
        name = requests.get("{}/{}"
                            .format(url, id)).json().get("username")
        req = requests.get("{}/{}/todos".format(url, id)).json()
        with open("{}.csv".format(id), mode="w", newline="") as f:
            csvfile = csv.writer(f, delimiter=",", quotechar='"',
                                 quoting=csv.QUOTE_ALL)
            csvfile.writerows([id, name, t.get("completed"), t.get("title")]
                              for t in req)
