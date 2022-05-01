#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Revision History:
    Animesh Bala Ani: Baseline Script.

"""

import traceback
import logging
from fastapi import HTTPException


def make_prediction(model, inputs):
    try:
        return inputs
    except:
        logging.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail="Internal Server Error")
