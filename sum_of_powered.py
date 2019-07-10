#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 16:11:27 2019

@author: bakunobu
"""

import numpy as np

def pythonsum(n):
    """
    As it is in Idris'es Numpy tutorial
    """
    a = list(range(n)) # simly range(n) doesn't work anymore
    b = list(range(n))
    c = []
    for i in range(len(a)):
        a[i] = i ** 2
        b[i] = i ** 3
        c.append(a[i] + b[i])
    
    return c


def python_gen_sum(n):
    """
    My version using generator
    """
    return [a ** 2 + a ** 3 for a in range(n)] # don't create too much variables


def numpy_sum(n):
    """
    NumPy solution
    """
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    c = a + b
    return c