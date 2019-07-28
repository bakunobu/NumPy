#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 22:36:36 2019

@author: bakunobu
"""

import numpy as np

def find_pivots(max_price, min_price, close_price):
    return (max_price + min_price + close_price) / 3


def fit_line(t, y):
    A = np.vstack([t, np.ones_like(t)]).T
    return np.linalg.lstsq(A, y)[0]


def sup_and_res(max_price, min_price, close_price, pivots):
    t = np.arange(len(close_price))
    sa, sb = np.fit_line(t, pivots - (max_price - min_price))
    ra, rb = np.fit_line(t, pivots + (max_price - min_price))
    support = sa * t + sb
    resistance = ra * t + rb
    return support, resistance


