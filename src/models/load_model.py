#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Revision History:
    Animesh Bala Ani: Baseline Script.

"""

from fastapi import HTTPException


def load_model():
    try:
        return None
    except:
        raise HTTPException(status_code=500, detail="Internal Server Error")