#!/bin/python3

import requests, json, os, stat, re
# from getpass import getpass
from bs4 import BeautifulSoup


session = requests.Session()
login_page_response = session.get('localhost:9000')
print(login_page_response.text)
# soup = BeautifulSoup(login_page_response.text, 'html.parser')
# authenticity_token = soup.find('input', attrs={'name': 'authenticity_token'})['value']
# print("---> ", authenticity_token)
with open("1337.html", "w") as f:
	f.write(login_page_response.text)
