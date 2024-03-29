#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 16:41:12 2019

@author: bakunobu

A simple performance test. Return the task's duration.
"""


from datetime import datetime

def find_duration(task, n):
    """
    task for an one-argument function, n for an argument
    """
    start = datetime.now()
    result = task(n)
    delta = datetime.now() - start
    return delta, result[-1]
   
    
