#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 13:42:50 2019

@author: bakunobu
"""


import numpy as np


def vwap(col_a, col_b):
    return np.average(col_a, weights=col_b)


def twap(data):
    t = np.arange(len(data))
    twap = np.average(data, weights=t)
    return twap
