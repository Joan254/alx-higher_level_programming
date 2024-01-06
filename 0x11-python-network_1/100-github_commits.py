#!/usr/bin/python3
"""Python script that takes 2 arguments in order to
list the 10 most recent commits on a given GitHub repository
Usage: ./100-github_commits.py <repository name> <repository owner>
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[2], sys.argv[1])
    rq = requests.get(url)
    commits = rq.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
