#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Revision History:
    Animesh Bala Ani: Baseline Script.

"""

from fastapi import FastAPI

from routers import router_template
from utils.load_model import load_model


model = load_model()
app = FastAPI()
app.include_router(router_template.create_router(model))
