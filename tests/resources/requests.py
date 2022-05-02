#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Revision History:
    Animesh Bala Ani: Baseline Script.

"""

import json
import requests


API_URL = "http://127.0.0.1:8000/template"
HEADERS = {"Content-Type":"application/json"}


with open('input.json') as f:
    inputs = json.load(f)

response = requests.post(API_URL, data=json.dumps(inputs), headers=HEADERS)

outputs = response.json()

print(outputs)
print(response.status_code)
