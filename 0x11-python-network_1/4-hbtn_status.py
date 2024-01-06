#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status
using the package requests"""
import requests


if __name__ == "__main__":
    rq = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(rq.text)))
    print("\t- content: {}".format(rq.text))
