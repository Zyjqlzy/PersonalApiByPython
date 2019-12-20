#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

url = "http://127.0.0.1:58080/personalMatters-api/login"
login_payload = {"username": "admin", "password": "123456"}
login_request = requests.post(url, login_payload)
token = login_request.json()['data']['token']
print(login_request.status_code)
print(token)

# if __name__ == "__main__":
