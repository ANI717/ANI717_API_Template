#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Revision History:
    Animesh Bala Ani: Baseline Script.

"""

import traceback
import logging


def load_model():
    try:
        return None
    except:
        logging.error(traceback.format_exc())
        return None
