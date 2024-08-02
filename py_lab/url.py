#!/bin/python3

from requests import get

r = get("http://getalien.tech")
print(r.status_code)

