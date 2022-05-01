#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Revision History:
    Animesh Bala Ani: Baseline Script.

"""

from fastapi import APIRouter
from models import input_pydantic_model, output_pydantic_model
from utils.make_prediction import make_prediction


def create_router(model):
    
    # initialize a router
    router = APIRouter(responses={404: {"description": "Not found"}},)
    
    # initialize POST request for router
    @router.post("/template")
    async def router_template(inputs: input_pydantic_model.MainModel):
        
        outputs = make_prediction(model, inputs.dict())
        
        return output_pydantic_model.MainModel(**outputs)
    
    return router
