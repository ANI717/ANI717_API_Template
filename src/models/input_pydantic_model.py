#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Revision History:
    Animesh Bala Ani: Baseline Script.

"""

from pydantic import BaseModel, AnyUrl, Field
from typing import List, Literal, Optional
from datetime import datetime


class DetailedInfo(BaseModel):
  date: datetime
  http_status: Literal[100,101,102,103,
                      200,201,202,203,204,205,206,207,208,226,
                      300,301,302,303,304,305,306,307,308,
                      400,401,402,403,404,405,406,407,408,409,
                      410,411,412,413,414,415,416,417,
                      418,421,422,423,424,425,426,428,429,431,451,
                      500,501,502,503,504,505,506,507,508,510,511] = Field(200)
  mime_type: Literal['text/html'] = Field('text/html')
  url: AnyUrl = Field('https://animeshani.com/')

class MainModel(BaseModel):
    name: str
    age: int
    info: bool
    detailed_info: Optional[List[DetailedInfo]]


if __name__ == "__main__":
    print(MainModel.schema_json(indent=4))
