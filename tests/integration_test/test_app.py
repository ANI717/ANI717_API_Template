#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Revision History:
    Animesh Bala Ani: Baseline Script.

"""

import json
import pytest
import requests


API_URL = "http://127.0.0.1:8000/template"
INPUTS_PATH = './tests/resources/input.json'
OUTPUTS_PATH = './tests/resources/output.json'
HEADERS = {"Content-Type":"application/json"}



def load_io(inputs_path, outputs_path):
    with open(inputs_path) as f:
        inputs = json.load(f)
    with open(outputs_path) as f:
        outputs = json.load(f)
    return inputs, outputs



@pytest.mark.app
def test_with_get_request():
    response = requests.get(API_URL)
    assert response.status_code == 405

@pytest.mark.app
def test_with_no_input():
    response = requests.post(API_URL)
    assert response.status_code == 422

@pytest.mark.app
def test_with_true_input(inputs_path=INPUTS_PATH, outputs_path=OUTPUTS_PATH):
    inputs, outputs = load_io(inputs_path, outputs_path)
    response = requests.post(API_URL, data=json.dumps(inputs), headers=HEADERS)
    assert response.status_code == 200
    assert response.json() == outputs

@pytest.mark.app
def test_with_additional_keys(inputs_path=INPUTS_PATH, outputs_path=OUTPUTS_PATH):
    inputs, outputs = load_io(inputs_path, outputs_path)
    inputs['email'] = 'animesh.ani@live.com'
    response = requests.post(API_URL, data=json.dumps(inputs), headers=HEADERS)
    assert response.status_code == 200
    assert response.json() == outputs

@pytest.mark.app
def test_with_missing_key(inputs_path=INPUTS_PATH, outputs_path=OUTPUTS_PATH):
    inputs, outputs = load_io(inputs_path, outputs_path)
    inputs.pop('name')
    response = requests.post(API_URL, data=json.dumps(inputs), headers=HEADERS)
    assert response.status_code == 422

@pytest.mark.app
def test_with_wrong_url(inputs_path=INPUTS_PATH, outputs_path=OUTPUTS_PATH):
    inputs, outputs = load_io(inputs_path, outputs_path)
    inputs['detailed_info'][0]['url'] = 'ANI717'
    response = requests.post(API_URL, data=json.dumps(inputs), headers=HEADERS)
    assert response.status_code == 422

@pytest.mark.app
def test_with_wrong_http_status(inputs_path=INPUTS_PATH, outputs_path=OUTPUTS_PATH):
    inputs, outputs = load_io(inputs_path, outputs_path)
    inputs['detailed_info'][0]['http_status'] = 'ANI717'
    response = requests.post(API_URL, data=json.dumps(inputs), headers=HEADERS)
    assert response.status_code == 422

@pytest.mark.app
def test_with_wrong_mime_type(inputs_path=INPUTS_PATH, outputs_path=OUTPUTS_PATH):
    inputs, outputs = load_io(inputs_path, outputs_path)
    inputs['detailed_info'][0]['mime_type'] = 'ANI717'
    response = requests.post(API_URL, data=json.dumps(inputs), headers=HEADERS)
    assert response.status_code == 422
    assert response.status_code == 422


if __name__ == "__main__":
    inputs_path = '../resources/input.json'
    outputs_path = '../resources/output.json'
    
    test_with_get_request()
    test_with_no_input()
    test_with_true_input(inputs_path, outputs_path)
    test_with_additional_keys(inputs_path, outputs_path)
    
    test_with_missing_key(inputs_path, outputs_path)
    test_with_wrong_url(inputs_path, outputs_path)
    test_with_wrong_http_status(inputs_path, outputs_path)
    test_with_wrong_mime_type(inputs_path, outputs_path)
    