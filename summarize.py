#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 15:52:30 2019

@author: bakunobu
"""


import numpy as np


def summarize(a, op_price, h_p, l_p, cl_price):
    monday_open = op_price[a[0]]
    week_high = np.max(np.take(h_p, a))
    week_low = np.min(np.take(l_p, a))
    friday_close = cl_price[a[-1]]
    return (monday_open, week_high, week_low, friday_close)
    