#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Revision History:
    Animesh Bala Ani: Baseline Script.

"""

from fastapi import APIRouter
from schema import input_schema
from schema import output_schema
from models.make_prediction import make_prediction


def create_router(model):
    
    router = APIRouter(responses={404: {"description": "Not found"}},)
    
    @router.post("/template")
    async def router_template(inputs: input_schema.MainModel):
        outputs = make_prediction(model, inputs.dict())
        return output_schema.MainModel(**outputs)
    
    return router