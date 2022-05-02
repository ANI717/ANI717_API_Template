#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Revision History:
    Animesh Bala Ani: Baseline Script.

"""

import os
import sys
import json
import pytest


if __name__ == '__main__':
    sys.path.append(os.path.join(os.getcwd(),'../../src'))
    INPUTS_PATH = '../resources/input.json'
    OUTPUTS_PATH = '../resources/output.json'
else:
    sys.path.append(os.path.join(os.getcwd(),'./src'))
    INPUTS_PATH = './tests/resources/input.json'
    OUTPUTS_PATH = './tests/resources/output.json'


# load input and output data
def load_io(inputs_path, outputs_path):
    with open(inputs_path) as f:
        inputs = json.load(f)
    with open(outputs_path) as f:
        outputs = json.load(f)
    return inputs, outputs


# functions for pytesting
@pytest.mark.utils
def test_load_model():    
    from ani717_api_template.utils.load_model import load_model
    assert load_model() == None

@pytest.mark.utils
def test_make_prediction(inputs_path=INPUTS_PATH, outputs_path=OUTPUTS_PATH):
    from ani717_api_template.utils.load_model import load_model
    from ani717_api_template.utils.make_prediction import make_prediction
    inputs, outputs = load_io(inputs_path, outputs_path)
    assert make_prediction(load_model(), inputs) == outputs
    
        
if __name__ == '__main__':
    test_load_model()
    test_make_prediction()
