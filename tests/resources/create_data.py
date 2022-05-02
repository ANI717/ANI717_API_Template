#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Revision History:
    Animesh Bala Ani: Baseline Script.

"""

from faker import Faker
import numpy as np
import json


Faker.seed(0)


fake = Faker() 


def create_data(x: int):
    
    data = []
    for i in range(0, x):
        data_i = {}
        data_i['name']= fake.name()
        data_i['age'] = np.random.randint(1,100)
        data_i['info'] = fake.pybool()
        data_i['detailed_info'] = [{
            'date': "2022-04-12T01:10:10.255000",
            'http_status': 200,
            'mime_type':'text/html',
            'url':'https://www.animeshani.com/',
            }]
        data.append(data_i)
    
    return data_i


if __name__=="__main__":
    data = create_data(1)
    with open('input.json', 'w') as f:
        json.dump(data, f)
